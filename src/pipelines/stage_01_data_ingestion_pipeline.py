from src.components.Data_ingestion import DataIngestion
from src.logger import logging
import sys
from src.config.configuration import ConfigurationManager
from src.exception import CustomException


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            data_config  = ConfigurationManager()
            data_ingestion_config = data_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
        except Exception as e:
            logging.info("Error occure {}".format(e))
            raise CustomException(e,sys)
        
