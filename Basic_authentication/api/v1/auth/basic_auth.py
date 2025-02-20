#!/usr/bin/env python3
"""Script contains Basic Auth Class that inherits auth class
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    This is a basic auth class. Uses basic auth
    to authenticate requests
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Method checks if authorization header has correct format
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        split_header = authorization_header.split()
        return split_header[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
        """
        Method decodes authorization credentials
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_str = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None
