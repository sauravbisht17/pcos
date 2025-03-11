import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Specifies the name of the log file.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Specifies the path of the logs directory.
os.makedirs(logs_path,exist_ok=True) #Creates the logs directory if it does not exist.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #Specifies the path of the log file.

logging.basicConfig(
    filename=LOG_FILE_PATH, #Specifies the file where log messages will be written.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #Specifies the format of log messages.
    level=logging.INFO, #Specifies the lowest-severity log message a logger will handle.
)