#!/usr/bin/env python3
"""
File contains function that obfuscates text
"""
import re


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        message = re.sub(f'{field}=[^;]+', f'{field}={redaction}', message)
    return message
