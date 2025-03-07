#!/usr/bin/env python3
""""""
import unittest
import client
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock


class TestGithubOrgClient(unittest.TestCase):
    """"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value="")
    def test_org(self, org_name: str):
        """"""
