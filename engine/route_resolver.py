# -----------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

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
