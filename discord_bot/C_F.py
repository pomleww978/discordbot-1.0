import time
import logging
from datetime import datetime
import json

def log() :
    logging.basicConfig(filename="CDR.txt", format="%(asctime)s %(message)s ", filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG) 

def log_logger(type,message) :
    if type == "info" :
        logging.info(f"[{type}]" + message)
    if type == "debug" :
        logging.debug(f"[{type}]" + message)
    if type == "warning" :
        logging.warning(f"[{type}]" + message)
    if type == "error" :
        logging.error(f"[{type}]" + message)
    if type == "critical" :
        logging.critical(f"[{type}]" + message)

def json_change_status(time_now) :
    file_path = 'status/config.json'
    with open (file_path , 'r') as json_file :
        data = json.load(json_file)
    data["status"]["bot_start_time"] = time_now
    data["status"]["mode"] = "active"
    with open(file_path , "w") as jsonFile:
        json.dump(data , jsonFile)

def on_start() :
    time_now = str(datetime.now())
    log()
    with open ("status/software_info.json" , 'r') as json_file :
        data = json.load(json_file)

    log_logger("info","discord bot version " + data["bot_version"] + " ITFRS(interferon sucerity)" + data['ITFRS_version'])
    log_logger("info", "start bot at" + time_now )
    log_logger("debug", "calling json_change_status function" )
    log_logger("debug", "calling logger function")
    log_logger("debug", "set bot status from inactive to active")
    json_change_status(time_now)
    print("discord bot version " + data["bot_version"] + " ITFRS(interferon sucerity)" + data['ITFRS_version'])
    print( "start bot at" + time_now )

def close_func() :

    now = datetime.now()
    close_time = now.strftime("%H:%M:%S")
    file = "status/config.json"
    log_logger("debug", "calling close_func function")
    
    with open (file , 'r') as json_file :
        data = json.load(json_file)
    data["status"]["mode"] = "inactive"
    data["status"]["last_active"] = close_time
    with open(file , 'w' ) as json_file :
        json.dump(data , json_file)
