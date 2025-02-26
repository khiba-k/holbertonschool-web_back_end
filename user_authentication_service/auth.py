#!/usr/bin/env python3
"""Script Auth Class"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Method hashes password and returns hash"""
    bytes_pw = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes_pw, salt)

    return hash
