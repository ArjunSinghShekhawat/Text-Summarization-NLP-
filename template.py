import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_file = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/entity/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipelines/__init__.py",
    "src/exception.py",
    "src/logging.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "app.py",
    "research/trials.ipynb",
    ".gitignore"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file_obj:
            pass
        logging.info(f"File {filepath} successfully created :")
    else:
        logging.info(f"This file is already exists {filepath}")


