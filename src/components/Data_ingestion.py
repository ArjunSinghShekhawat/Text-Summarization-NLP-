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
        if (not os.path.exists(self.config.local_data_file)):

            filename,header = request.urlretrieve(
                filename=self.config.local_data_file,
                url=self.config.source_URL
            )
            logging.info(f"File {filename} Successfully download with information {header}")

        else:
            logging.info(f"File {filename} already exists with size {os.path.getsize(filename=filename)}")

    def extract_zip_file(self):


        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)


            

