## **Project Overview**

**Project Name:** BluePI engine

**Description:**
A Python + FastAPI engine that dynamically converts JSON flow definitions into backend routes. Designed to be extensible via nodes for HTTP, database, auth, logic, and more. Ideal for building visual backend workflow tools, low-code platforms, or automation engines.

**Key Features:**

* JSON → FastAPI route resolver
* Modular node system (OOP-based)
* Async-first execution
* Easy to extend with custom nodes
* Unit-tested core engine

**Status:** Prototype / Alpha / Beta / Stable

---

## **Getting Started**

### **Prerequisites**

* Python 3.11+
* pip
* (Optional) PostgreSQL / MongoDB if using database nodes

### **Installation**

```bash
# Clone the repo
git clone https://github.com/<username>/nodeflow-engine.git
cd nodeflow-engine

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### **Run the Engine**

```bash
uvicorn engine.main:app --reload
```

Visit [http://localhost:8000/hello](http://localhost:8000/hello) to test the sample flow.

---

## **Project Structure**

```
nodeflow/
├─ engine/
│  ├─ main.py           # FastAPI app + flow resolver
│  ├─ node_base.py      # Base Node class
│  ├─ nodes/            # Node implementations
│  │   ├─ http_in.py
│  │   ├─ log.py
│  │   └─ http_response.py
│  └─ flow.json         # Example JSON flow
├─ tests/               # Unit tests
├─ demos/               # Demo flows / examples
├─ requirements.txt
├─ .gitignore
└─ README.md
```

---

## 4. **JSON Flow Definition**

### **Nodes**

Each node must have:

* `id`: Unique identifier
* `type`: Node type (must match a registered node class)
* Node-specific configuration (`route`, `message`, `body`, etc.)

**Example:**

```json
{
  "nodes": [
    {"id": "1", "type": "http_in", "route": "/hello"},
    {"id": "2", "type": "log", "message": "Incoming request"},
    {"id": "3", "type": "http_response", "body": "Hello World!"}
  ],
  "connections": [
    ["1", "2"],
    ["2", "3"]
  ]
}
```

### **Connections**

Connections define the directed flow:

```
[Source Node ID] -> [Target Node ID]
```

The engine executes nodes in the order of connections.

---

## **Node Development Guide**

### **Base Node Class**

All nodes should inherit from `engine.node_base.Node`:

```python
class Node:
    type: str = "base"
    def __init__(self, node_id: str, config: dict):
        self.id = node_id
        self.config = config
    async def run(self, context: dict, next_fn):
        raise NotImplementedError
    def init_route(self, app, next_fn):
        pass
```

### **5.2 Example Node**

```python
from engine.node_base import Node

class LogNode(Node):
    type = "log"
    async def run(self, context, next_fn):
        print(self.config.get("message", ""), context.get("data"))
        await next_fn(self.id, context)
```

###  **Node Lifecycle**

* `init_route()`: Optional, for HTTP entry nodes
* `run()`: Executed sequentially in flow
* `context`: Shared data dictionary across nodes

---

## **Testing**

### **Run Unit Tests**

```bash
pytest -v
```

### **Recommended Tests**

* Route registration (`http_in` nodes)
* Data passing between nodes
* Invalid node type handling
* Flow execution order

---

## **Extending the Engine**

* Add new node types in `engine/nodes/`
* Ensure node `type` is unique
* Update `flow.json` to include new node types
* Optionally add unit tests for new nodes

---

## **Examples & Demos**

* Place reusable flow definitions in `demos/`
* Example flows:

  * HTTP → Log → Response
  * HTTP → DB Query → Transform → Response
  * HTTP → Conditional → Response

---

Perfect — that’s a very common and professional open-source workflow. Here’s the updated **Contribution Guidelines** section for your docs:

---

## **Contribution Guidelines**

* **Use Issues First:**

  * For **major features**, architectural changes, or significant documentation updates, open an issue **before** starting work.
  * Describe your proposed changes, rationale, and any potential impact.
  * This ensures discussion, feedback, and alignment with maintainers.

* **Fork the Repo:**

  * Create a personal fork of the repository.

* **Create a Feature Branch:**

  * Branch off from `main` using a descriptive name (e.g., `feature/db-node`, `docs/new-node-types`).

* **Implement Your Changes:**

  * Add unit tests for any new nodes or logic.
  * Update documentation to reflect new functionality.
  * Follow PEP8 / Python style guidelines.

* **Submit a Pull Request (PR):**

  * Reference the corresponding issue in the PR description.
  * Provide a clear summary of changes and impact.
  * Ensure all tests pass before submitting.

* **Review Process:**

  * Maintainers or contributors will review, provide feedback, and approve PRs.

---
