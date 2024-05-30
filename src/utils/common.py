import os
from src.logger import logging
from src.exception import CustomException
import yaml
import sys
from pathlib import Path
from typing import Any
from box import ConfigBox
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(filepath:Path)->ConfigBox:
    """
    This function is used to read yaml file

    Args:
        filepath
    
    return:
          exception when file is empty
    """

    try:
        with open(filepath) as file_obj:
            content = yaml.safe_load(file_obj)
            logging.info(f"Yaml file {filepath} successfully created !")

            return ConfigBox(content)
        
    except Exception as e:

        logging.info("Error Occure {}".format(e))
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directories(filedir:list,verbose=True):
    """
    This function is used to create file directory

    Args:
        filedir:list

    return:
          None
    """
    for filepath in filedir:
        os.makedirs(filepath,exist_ok=True)

        if verbose:
            logging.info(f"Filedir Successfully created {filepath}")

@ensure_annotations
def get_size(filepath:Path)->str:
    """
    This function is used to get the filesize

    Args:
        filepath
    
    return:
         size of the file         
    """

    size = os.path.getsize(filepath)

    return f"~ {size} KB"

