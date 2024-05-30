from src.logger import logging
from src.exception import CustomException
from src.components.Data_validation import DataValidationConfig
from src.config.configuration import ConfigurationManager
import os
import sys


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

            config =  ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidationConfig(data_validation_config)
            data_validation.validates_all_files_exists()

        except Exception as e:
            logging.info("Error occure {}".format(e))
            raise CustomException(e,sys)
        