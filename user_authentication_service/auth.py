#!/usr/bin/env python3
"""Script Auth Class"""
from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Method hashes password and returns hash"""
    bytes_pw = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes_pw, salt)

    return hash


def _generate_uuid() -> str:
    """Method generates a unique id"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method registers a new user"""
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists:
                raise ValueError(f"User {email} already exists")

        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email, hashed_pass)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Method validates user creds"""
        try:
            user = self._db.find_user_by(email=email)
            pass_to_bytes = password.encode("utf-8")
            return bcrypt.checkpw(pass_to_bytes, user.hashed_password)
        except NoResultFound:
            return False
