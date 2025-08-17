#!/usr/bin/env python3
"""10-update_topics: Update the topics of a school document"""

def update_topics(mongo_collection, name, topics):
    """
    Update all documents in a collection with a specific school name,
    setting the 'topics' field to the provided list of topics.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        dict: The result of the update_many operation.
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return None

    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.raw_result
