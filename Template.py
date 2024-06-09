import os 
from pathlib import Path 
import logging
 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/run_local.py",
    "src/helper.py",
    "model/instruction.txt",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb"]


for file in list_of_files:

    file = Path(file)
    filedir,filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"create directory; {filedir} for the file: {filename}")

    if (not os.path.exists(file)or os.path.getsize(file) == 0):
        with open (file, 'w') as f:
            pass
            logging.info(f"Crating empty file:{file}")

    else:
        logging.info(f"{file} is alredy existing") 




