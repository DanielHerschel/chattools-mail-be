""" This module is used to read and parse YAML files. """


from typing import Any
from yaml import safe_load


def get_yaml_data(file_path: str) -> Any:
    """ This function reads and parses a YAML file.
    
    Parameters:
        file_path: str - The full/relative path to the YAML file.
    
    Returns:
    Optional[Dict[Any, Any]] - The parsed data loaded from the file or None if an error has occured.
    """
    with open(file_path) as yaml_file:
        return safe_load(yaml_file)
