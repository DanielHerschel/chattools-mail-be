""" This module is reponsible to handle config files. """


import yaml
import logging
from typing import Dict, Optional
import os

from utils.yaml_handler import get_yaml_data
from utils.dict_value_injector import inject_value


def load_configutation() -> Optional[Dict]:
    """ Load the app configuration file.
    
    Returns:
    Optional[Dict]: The loaded configuration file.
    """
    configuration_path = os.path.join(".", "appsettings.yaml")

    if not os.path.exists(configuration_path):
        logging.debug(f"Could not find appsettings.yaml in {configuration_path}")
        return None

    try:
        config = get_yaml_data(configuration_path)
    except yaml.parser.ParseError:
        logging.debug(f"Could not parse yaml in {configuration_path}")
        return None
    
    for key, value in os.environ.items():
        if any([key.startswith(k) for k in config.keys()]):
            config_path = key.split('__')
            inject_value(config, config_path, value)
    
    return config
