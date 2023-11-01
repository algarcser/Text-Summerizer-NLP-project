import os
import sys
import logging

"""
This will display the following information when you are logging:
    the timestamp of the operation
    the level of the operation
    the module that is doing the operation
    the custom message created    
"""

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # we will save the log in a file
        logging.StreamHandler(sys.stdout) # we will also show in the console the log so that we can check it. 
    ]
)

logger = logging.getLogger("textSummarizerLogger")