#!/usr/bin/env python3
"""Script contains cache class that uses Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class handles caching data using Redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis(host='127.0.0.1',
                                  port=6379, decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method stores data with unique id key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
