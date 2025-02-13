#!/usr/bin/env python3
"""
Script filters values in incoming log records
"""
import logging
import re
from typing import List, Tuple
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "id")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Redacts specified fields in a message."""
    pattern = (f'({"|".join(map(re.escape, fields))})=[^ {separator}]*')
    return re.sub(pattern,
                  lambda match: f'{match.group(1)}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]):
        """
        Initialize the formatter with specific fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Functions returns a custom logger object

    Returns:
        logging.Logger: instance of a logger object
    """
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    user_data.propagate = False

    user_data_handler = logging.StreamHandler()
    user_data_handler.setLevel(logging.INFO)

    user_data_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    user_data.addHandler(user_data_handler)

    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to MySQL database using environment variables
    Returns a MySQLConnection object
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

    return connection
