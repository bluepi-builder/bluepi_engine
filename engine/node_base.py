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

import uuid
from abc import ABC, abstractmethod


class Node(ABC):
    """Base class for all node types in the flow."""

    def __init__(self, id=None, node_type=None):
        self.id = id or str(uuid.uuid4())
        self.type = node_type
        self.inputs = []
        self.outputs = []

    @abstractmethod
    def execute(self, context: dict):
        """Perform this node’s action."""
        pass

    def connect_to(self, other_node):
        """Establish a connection to another node."""
        self.outputs.append(other_node)
        other_node.inputs.append(self)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} type={self.type}>"
