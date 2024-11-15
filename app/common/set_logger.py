import os
import json
import logging
import logging.config

def set_logger() -> bool:
    try:
        with open(os.path.join(os.path.dirname(__file__), 'logging.json'), 'r') as f:
            logging.config.dictConfig(json.load(f))
        return True
    except:
        print('Failed logger settings')
        return False
