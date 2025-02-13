#!/usr/bin/env python3
"""Script contains function that hashes password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function hashes password and returns it as a salted hash

    Args:
        password (str): The password that has beeen inserted by user

    Returns:
        bytes: The data type of the password after hashing
    """
    encoded = password.encode('utf-8')
    passwrd = bcrypt.hashpw(password, bcrypt.gensalt())
    return passwrd
