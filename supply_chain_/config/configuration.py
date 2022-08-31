# from supply_chain_.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
# from supply_chain_.logger import logging
# from supply_chain_.exception import supply_chain_exception
# from supply_chain_.constant import *
# from supply_chain_.util.util import *
# import os,sys

# class Configuration:
#     def __init__(self,config_file_path:str=CONFIG_FILE_PATH,current_time_stamp:str=CURRENT_TIME_STAMP) -> None:
#         try:
#             self.config_info=read_yaml_file(file_path=config_file_path)
#             self.training_pipeline_config=self.get_training_pipeline_config()
#             self.timestamp=current_time_stamp
#         except Exception as e:
#             raise supply_chain_exception(e,sys) from e
#     def get_data_ingestion_config(self) -> DataIngestionConfig:

