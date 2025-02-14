#!/usr/bin/env python3
"""Script contains auth template class
"""
from flask import request


class Auth:
    """Class is a template of the auth system
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require auth public method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization header public method
        """
        return None

    def current_user(self, request=None) -> None:
        """
        Current user public method
        """
        return None
