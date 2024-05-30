from src.logger import logging
from src.exception import CustomException
from src.config.configuration import ConfigurationManager
from src.components.Data_transformation import DataTransformation
import sys

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()

        except Exception as e:
            logging.info("Error Occure {}".format(e))
            raise CustomException(e,sys)
