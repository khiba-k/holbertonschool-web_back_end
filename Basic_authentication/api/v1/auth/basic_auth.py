#!/usr/bin/env python3
"""Script contains Basic Auth Class that inherits auth class
"""
from flask import request
from typing import List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    pass
