"""
File: node.py

Node classes for one-way linked structures 
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
