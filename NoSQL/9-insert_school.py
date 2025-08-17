#!/usr/bin/env python3
"""9-insert_school: Insert a new document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
