import yaml
import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file) or {}
    except:
        return {}