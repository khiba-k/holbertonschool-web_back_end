#!/usr/bin/env python3
"""Script contains tests for the client module"""
import unittest
import client
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class tests GitHubOrgClient Method(s)"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value="")
    def test_org(self, org_name: str, mock_get: Mock):
        """Method tests GithubOrgClient org method"""

        mock_get.return_value = {"id": 1}

        org_client_instance = GithubOrgClient(org_name)
        result = org_client_instance.org

        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(result, {"id": 1})
        mock_get.assert_called_once_with(expected_url)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: Mock):
        """"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}

        org_client_inst = GithubOrgClient("google")

        result = org_client_inst._public_repos_url

        self.assertEqual(result,  "https://api.github.com/orgs/google/repos")
