#!/usr/bin/env python3
"""
Task 0: Regex-ing

This module provides a function to obfuscate specific fields in log messages.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Redacts specified fields in a message.

    Args:
        fields (list[str]): List of field names to redact.
        redaction (str): Replacement text for redacted values.
        message (str): The input message containing key-value pairs.
        separator (str): The separator between key-value pairs

    Returns:
        str: The message with specified fields redacted.
    """
    for field in fields:
        message = re.sub(rf'{field}=[^;]+', rf'{field}={redaction}', message)
    return message
