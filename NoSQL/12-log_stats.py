#!/usr/bin/env python3
"""
Script to display statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats(numbers: int) -> int:
    """
    Returns the count of documents in the Nginx logs collection
    that match the given query.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(numbers)


def main():
    """
    Displays various statistics about Nginx logs stored in MongoDB
    """
    print(f"{log_stats({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {log_stats({'method': 'GET'})}")
    print(f"\tmethod POST: {log_stats({'method': 'POST'})}")
    print(f"\tmethod PUT: {log_stats({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {log_stats({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {log_stats({'method': 'DELETE'})}")
    print(f"{log_stats({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()