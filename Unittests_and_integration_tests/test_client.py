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
        """Method tests _public_repos_url property"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}

        org_client_inst = GithubOrgClient("google")

        result = org_client_inst._public_repos_url

        self.assertEqual(result,  "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ([
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None},
        ], ["repo1", "repo2", "repo3"])
    ])
    @patch("client.get_json")
    def test_public_repos(self, payload, expected, mock_get_json: Mock) -> None:
        """Method tests """
        mock_get_json.return_value = payload

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "https://api.github.com/orgs/google/repos"

            client_inst = GithubOrgClient("google")

            result = client_inst.public_repos()

            self.assertEqual(result, expected)
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")
