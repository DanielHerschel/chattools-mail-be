import pytest
import yaml

from src.utils.yaml_handler import get_yaml_data


def test_validation_yaml():
    with pytest.raises(FileNotFoundError):
        get_yaml_data(file_path="tests/data/non_existing_file.yaml")

    with pytest.raises(yaml.parser.ParserError):
        # only show the first error
        get_yaml_data(file_path="tests/data/test_yaml_file.yaml")   
