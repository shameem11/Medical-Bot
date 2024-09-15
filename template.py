import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(message)s:")

list_of_files =[
<<<<<<< HEAD
    "src/ __init__.py",
    "src/ prompt.py",
    "src/ loader.py"
    "setup.py",
    "research/Training.ipynb",
    "templates/bot.html",
    "static/style.css"
=======
    "src/__init__.py",
    "src/prompt.py",
    "setup.py",
    "research/Training.ipynb",
    "streamlit.py",
>>>>>>> origin/main
    "store_index.py"

]

for file_path in list_of_files:
<<<<<<< HEAD
    file_path=Path(file_path) # path class help to detect the OS this privent the unicorn error 
=======
    file_path=Path(file_path) # path class help to detect the the OS
>>>>>>> origin/main
    filedir,filename = os.path.split(file_path)

    if filedir !="":
        os.makedirs(file_path)
        logging.info(f"creating directory;{filedir}for the file {filename}")


    if (not os.path.exists(file_path)):
        with open(file_path,'w') as f:
            pass 
        logging.info(f"creating empty file {file_path}")
    else:
        logging.info(f"{filename} is already created")


