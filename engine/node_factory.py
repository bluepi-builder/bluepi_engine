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

from node_base import Node


class PathNode(Node):
    def __init__(self, id, method, path):
        super().__init__(id, "path")
        self.method = method
        self.path = path

    def execute(self, context):
        context["method"] = self.method
        context["path"] = self.path
        print(f"[PathNode] Handling {self.method} {self.path}")
        return context


class AuthNode(Node):
    def __init__(self, id, strategy):
        super().__init__(id, "auth")
        self.strategy = strategy

    def execute(self, context):
        print(f"[AuthNode] Authenticating via {self.strategy}")
        context["auth"] = f"Authenticated using {self.strategy}"
        return context


class LogNode(Node):
    def __init__(self, id, message):
        super().__init__(id, "log")
        self.message = message

    def execute(self, context):
        print(f"[LogNode] {self.message}")
        return context


class DBNode(Node):
    def __init__(self, id, action, table, fields):
        super().__init__(id, "db")
        self.action = action
        self.table = table
        self.fields = fields

    def execute(self, context):
        print(f"[DBNode] {self.action.upper()} into {self.table} -> {self.fields}")
        context["db_action"] = (self.action, self.table, self.fields)
        return context


class CallbackNode(Node):
    def __init__(self, id, code):
        super().__init__(id, "callback")
        self.code = code

    def execute(self, context):
        print(f"[CallbackNode] Executing: {self.code}")
        context["response"] = self.code
        return context


class NodeFactory:
    NODE_MAP = {
        "path": PathNode,
        "auth": AuthNode,
        "log": LogNode,
        "db": DBNode,
        "callback": CallbackNode,
    }

    @classmethod
    def create_node(cls, node_data: dict):
        node_type = node_data.get("type")
        node_class = cls.NODE_MAP.get(node_type)

        if not node_class:
            raise ValueError(f"Unknown node type: {node_type}")

        return node_class(**{
            k: v for k, v in node_data.items()
            if k in node_class.__init__.__code__.co_varnames
        })
