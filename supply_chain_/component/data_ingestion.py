from supply_chain_.entity.config_entity import DataIngestionConfig
import sys,os
from supply_chain_.exception import supply_chain_exception
from supply_chain_.constant import *
from supply_chain_.logger import logging
from supply_chain_.entity.artifact_entity import DataIngestionArtifact
import numpy as np
import pandas as pd
from supply_chain_.util.util import *
from sklearn.model_selection import train_test_split
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.raw_data_dir,exist_ok=True)
        except Exception as e:
            raise supply_chain_exception(e,sys)
    def get_data_from_database(self):
        try:
            cloud_config= {'secure_connect_bundle': 'F:\Projects\Dataset\secure-connect-supply-chain (1).zip'}
            auth_provider = PlainTextAuthProvider('YhSESSUCnZINLjqKowOeDZNt', '0PgD5PFX8L6FkpFnatUAF3NBA.ruwbtUWj52Mte-YdnMyOwh.PLXZs2S9O3Zoo+9.bnJ6TJ8kNa6bvmkB-RkivfjCxxj7mo3A8HztdKz-47s2OZZrQ0,i+W0cJ8qi304')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect("data")

            # row = session.execute("SELECT * FROM forest_cover.train").one()
            session.row_factory = pandas_factory
            session.default_fetch_size = None
            query = "SELECT * FROM supply_data_ineuron_ai_database_proj12"
            rslt = session.execute(query, timeout=None)
            df = rslt._current_rows
            df.to_csv(os.path.join(self.data_ingestion_config.raw_data_dir,"dumped_data.csv"),index=False)
        except Exception as e:
            raise supply_chain_exception(e,sys) from e


    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
            file_name=os.listdir(os.path.join(PATH_READ_LATEST_INGESTION_DATA,os.listdir(PATH_READ_LATEST_INGESTION_DATA)[(len(os.listdir(PATH_READ_LATEST_INGESTION_DATA)))-1],"raw_data"))[0]

            supply_chain_file_path = os.path.join(raw_data_dir,file_name)


            logging.info(f"Reading csv file: [{supply_chain_file_path}]")
            supply_chain_data_frame = pd.read_csv(supply_chain_file_path)

            df_train,df_test = train_test_split(supply_chain_data_frame,test_size=0.2, random_state=0)

            logging.info(f"Splitting data into train and test")

            train_file_path=os.path.join(self.data_ingestion_config.ingested_train_dir,"train_data.csv")
            df_train.to_csv(train_file_path,index=False)
            test_file_path=os.path.join(self.data_ingestion_config.ingested_test_dir,"test_data.csv")
            df_test.to_csv(test_file_path,index=False)

            data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,test_file_path=test_file_path,is_ingested=True,message="Data Ingested")
            return data_ingestion_artifact
        except Exception as e:
            raise supply_chain_exception(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            self.get_data_from_database()
            return self.split_data_as_train_test()
        except Exception as e:
            raise supply_chain_exception(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")