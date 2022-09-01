from supply_chain_.config.configuration import Configuration
from supply_chain_.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from supply_chain_.logger import logging
from supply_chain_.component.data_ingestion import DataIngestion
# from supply_chain_.component.data_validation import DataValidation
# from supply_chain_.component.data_transformation import DataTransformation
# from supply_chain_.component.model_trainer import ModelTrainer
from supply_chain_.entity.artifact_entity import *
from supply_chain_.exception import supply_chain_exception
from supply_chain_.constant import *
from supply_chain_.util.util import *
import sys

class Pipeline:
    def __init__(self, config: Configuration ) -> None:
        self.config=config()
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise supply_chain_exception(e, sys) from e


    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            return "done"
        except Exception as e:
            raise supply_chain_exception(e,sys) from e 