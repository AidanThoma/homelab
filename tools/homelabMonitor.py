"""
title: Homelab Prometheus Monitor
description: Read CPU, RAM, disk, network, container and Proxmox metrics from Prometheus.
"""

import requests
from urllib.parse import quote


class Tools:
    def __init__(self):
        self.prometheus_url = "http://192.168.4.3:9090"

    def query_prometheus(self, query: str) -> dict:
        """
        Query the user's live Prometheus homelab monitoring server.

        The Prometheus URL and connection details are already configured
        internally. NEVER ask the user for the Prometheus URL, credentials,
        or connection information.

        Use this tool whenever the user asks for live homelab metrics such as
        CPU, RAM, memory, disk, networking, Docker, Proxmox, or server status.

        :param query: The PromQL query to run.
        :return: The live Prometheus API result.
        """

        response = requests.get(
            f"{self.prometheus_url}/api/v1/query",
            params={"query": query},
            timeout=10,
        )

        response.raise_for_status()
        return response.json()

    def get_targets(self) -> dict:
        """
        Get the current UP/DOWN state of monitored Prometheus targets.
        """

        url = f"{self.prometheus_url}/api/v1/query"

        response = requests.get(url, params={"query": "up"}, timeout=10)

        response.raise_for_status()

        return response.json()
