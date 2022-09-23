from typing import Dict, Any, List


def inject_value(data: Dict[Any, Any], path: List[Any], value: Any):
    """ This function injects a given value in the given dictionary
        at a given path.
        
    If the value exists, replace the new value with the old one.
    The function will only replace values, not create new ones.

    Params:
        data: Dict[Any, Any] - The dictionary we want to modify.
        path: List[str] - The patht to the value (in the dictionary).
        value: Any - The value we want to add.
    
    Raises:
        IndexError: If it was not able to insert the value.
        KeyError: If the path is invalid.
    """
    for key in path[:-1]:
        data = data[key]
    
    try:
        data[path[-1]] = value
    except IndexError as error:
        # If the path specified is out of range, append the value as a list.
        if path[-1] == len(data):
            data += [value]
        else:
            raise error
