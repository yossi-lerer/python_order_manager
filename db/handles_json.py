import json
import os
import logging
logger = logging.getLogger(__name__)

def add_data_to_json(file_path, new_record: dict):
    logger.info(f"call to the function add_data_to_json")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            record = json.dumps([new_record], indent=2)
            f.write(record)
    else:
        with open(file_path, "r") as f:
            data = f.read()
            data = json.loads(data)
            data.append(new_record)

        with open(file_path, "w") as f:
            record = json.dumps(data, indent=4)
            f.write(record)

def update_json(file_path, data):
    logger.info(f"call to the function update_json")
    with open(file_path, "w") as f:
        record = json.dumps(data, indent=4)
        f.write(record)

def get_data_from_json(file_path):
    logger.info(f"call to the function get_data_from_json")
    try:
        with open(file_path, "r") as f:
            data = f.read()
            data = json.loads(data)
        return data
    except FileNotFoundError:
        return []
    except:
        logger.warning(f"the json file defective the program ended")
        print("the json file defective")
        exit()
            


