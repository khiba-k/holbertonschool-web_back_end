#!/usr/bin/env python3
"""Script contains auth template class
"""
from flask import request


class Auth:
    """Class is a template of the auth system
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
