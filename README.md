# northwind-python-client

Python client for the [Northwind data platform](https://northwind.kbird.ai/) —
pipelines, dashboards and webhooks without running infrastructure.

- API reference: https://northwind.kbird.ai/api-docs
- Quickstart: https://northwind.kbird.ai/docs/quickstart

## Install

```bash
pip install -r requirements.txt
```

## Usage

```python
import os
from northwind_client import NorthwindClient

client = NorthwindClient(api_key=os.environ["NORTHWIND_API_KEY"])
print(client.list_workspaces())
```
