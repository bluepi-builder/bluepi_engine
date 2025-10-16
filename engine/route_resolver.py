import json
import logging

def resolve_nodes(json_path:str):
    """
    Resolves the nodes (NO CONNECTIONS ARE INFERRED)

    Args:
        json_path (str): path to json file
    
    Returns:
        dictionary: map of nodes
    """

    try:
        with open(json_path, "r+") as file:
            return json.loads(file.read())["nodes"]

    except FileNotFoundError as err:
        logging.error(f"faced '{err}' while trying to read flow file")
    
def resolve_connections(json_path:str):
    """
    Resolves the connections 

    Args:
        json_path (str): path to json file
    
    Returns:
        dictionary: map of nodes
    """

    try:
        with open(json_path, "r+") as file:
            return json.loads(file.read())["connections"]

    except FileNotFoundError as err:
        logging.error(f"faced '{err}' while trying to read flow file")
