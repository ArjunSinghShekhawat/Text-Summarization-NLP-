from src.config.configuration import ConfigurationManager
from src.entity.config_entity import DataIngestionConfig
import os
import urllib.request as request
from src.logger import logging
import zipfile


class DataIngestion:
    
    def __init__(self,config=DataIngestionConfig):
        self.config = config

    def download_file(self):
        filepath = self.config.local_data_file  # Ensure filepath is defined
        
        if not os.path.exists(filepath):
            filepath, header = request.urlretrieve(
                filename=filepath,
                url=self.config.source_URL
            )
            
            logging.info(f"File {filepath} successfully downloaded with information {header}")
        else:
            logging.info(f"File {filepath} already exists with size {os.path.getsize(filepath)}")


    def extract_zip_file(self):


        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)


            

