#!/usr/bin/env python3
"""pymongo module"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """provide logs stats of nginx collection saved in a
    mongoDB using a list of methods

    Args:
        mongo_collection (Collection): mongo collection
    """
    all_logs = mongo_collection.count_documents({})
    path_status = mongo_collection.count_documents({"path": "/status"})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    nginx_counter = mongo_collection.count_documents

    print(all_logs, 'logs')
    print('Methods:')
    for method in methods:
        print(f"\tmethod {method}:", nginx_counter({"method": method}))
    print(path_status, "status check")


if __name__ == "__main__":
    nginx_coll = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_coll)
