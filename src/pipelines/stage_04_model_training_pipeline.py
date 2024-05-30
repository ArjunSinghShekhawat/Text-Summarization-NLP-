from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.entity.config_entity import ModelTrainingConfig
from src.config.configuration import ConfigurationManager
from src.components.Model_training import ModelTrainer

class ModelTrainerPipeline:
    
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()

        except Exception as e:

            logging.info("Error Occure {}".format(e))
            raise CustomException(e,sys)