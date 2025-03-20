#!/usr/bin/env python3
"""Script contains cache class that uses Redis"""
import redis
import uuid
from typing import Union, Callable, Optional, TypeVar, cast
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator that count
    how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Increments the count every time the method is called
        Returns
        - the value returned by the original method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class handles caching data using Redis"""

    def __init__(self) -> None:
        # Initialize Redis without decode_responses to get bytes
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method stores data with unique id key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        """
        Retrieve data from Redis and optionally apply a conversion function."""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)
