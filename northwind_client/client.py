"""Northwind data platform API client."""
import requests

from .config import API_BASE, API_KEY, DEFAULT_TIMEOUT


class NorthwindClient:
    def __init__(self, api_key=None, timeout=DEFAULT_TIMEOUT):
        self.api_key = api_key or API_KEY
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": "Bearer " + self.api_key}
        )

    def list_workspaces(self):
        r = self.session.get(API_BASE + "/workspaces", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def create_source(self, type_, name):
        r = self.session.post(
            API_BASE + "/sources",
            json={"type": type_, "name": name},
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def run_sync(self, source_id):
        r = self.session.post(
            API_BASE + "/syncs/%s/run" % source_id, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def list_runs(self, source_id):
        r = self.session.get(
            API_BASE + "/syncs/%s/runs" % source_id, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def delete_source(self, source_id):
        r = self.session.delete(
            API_BASE + "/sources/%s" % source_id, timeout=self.timeout
        )
        r.raise_for_status()
