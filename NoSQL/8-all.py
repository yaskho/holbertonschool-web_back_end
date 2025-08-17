#!/usr/bin/env python3
"""8-all: List all documents in a collection"""

def list_all(mongo_collection):
    """
    List all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.

    Returns:
        list: A list of documents (dictionaries) in the collection. Empty list if none.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
