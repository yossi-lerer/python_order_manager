import json
import os
# "./db/demofile.json"

def add_data_to_json(file_path, new_record: dict):
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
                
def get_data_from_json(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        data = json.loads(data)
    return data



