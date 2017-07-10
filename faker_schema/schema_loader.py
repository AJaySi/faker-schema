import json


def load_json_from_file(file_path):
    """Load schema from a file"""
    try:
        with open(file_path) as f:
            json_data = json.load(f)
    except ValueError as e:
        raise ValueError('Given file {} is not a valid JSON file: {}'.format(json_file, e))
    else:    
        return json_data


def load_json_from_string(string):
    """Load schema from string"""
    try:
        json_data = json.loads(string)
    except ValueError as e:
        raise ValueError('Given string is not valid JSON: {}'.format(e))
    else:    
        return json_data