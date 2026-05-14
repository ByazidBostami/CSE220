class Node:
    def __init__(self, key, value = None, next = None):
        self.key = key 
        self.value = value 
        self.next = next 

class HashTableExample:
    def __init__(self, size = 5):
        self.size = size 
        self.table = [None]* self.size 

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value% self.size 
    