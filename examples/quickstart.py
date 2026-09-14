import os

from northwind_client import NorthwindClient

client = NorthwindClient(api_key=os.environ["NORTHWIND_API_KEY"])
print(client.list_workspaces())
