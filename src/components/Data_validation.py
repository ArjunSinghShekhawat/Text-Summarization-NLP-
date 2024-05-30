from src.entity.config_entity import DataValidationConfig
from src.config.configuration import ConfigurationManager
import os
import sys
from src.logger import logging
from src.exception import CustomException

class DataValidationConfig:
    def __init__(self,config=DataValidationConfig):
        self.config = config

    def validates_all_files_exists(self)->bool:
        logging.info("I am enter im valdation all files exists function")
        
        try:
            validates_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:

                if file not in self.config.ALL_REQUIRED_FILES:
                    validates_status = False

                    with open(self.config.STATUS_FILE,"w") as file_obj:
                        file_obj.write(f"Validation Status : {validates_status}")

                else:
                    validates_status=True
                    
                    with open(self.config.STATUS_FILE,"w") as file_obj:
                        file_obj.write(f"Validation Status : {validates_status}")

            return validates_status
        
        except Exception as e:
            logging.info(f"File Status {validates_status}")
            raise CustomException(e,sys)


