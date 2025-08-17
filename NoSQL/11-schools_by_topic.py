#!/usr/bin/env python3
"""11-schools_by_topic: Return a list of schools having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Return all documents in the collection that contain a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        list: List of school documents containing the topic. Empty list if none found.
    """
    if mongo_collection is None or not topic:
        return []

    # Query for documents where the 'topics' list contains the given topic
    return list(mongo_collection.find({"topics": topic}))
