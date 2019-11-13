from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max = limit
        self.storage = DoublyLinkedList()
        self.size = self.storage.length
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
# I think I need to remove a node or key:value pair here

    def get(self, key):
        # print("---DICTIONARY---", self.storage_dict)
        if self.storage_dict.get(key) != None:
            # set node to be the head
            self.storage.move_to_front(self.storage_dict.get(key))
        # return its value
            return self.storage_dict.get(key).value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if above limit, delete from end of list
        # print("\n---DICTIONARY---", self.storage_dict)
        # if self.storage.tail:
        #     print("TAIL", self.storage.tail.key)

        # if key already exists, override (delete old node and make new)
        if key in self.storage_dict:
            # removes from linked list
            self.storage.delete(self.storage_dict[key])
            # adds new node to head of linked-list
            self.storage.add_to_head(key, value)
            # update dictionary with new value for key
            self.storage_dict[key] = self.storage.head
        else:
            if self.storage.length >= self.max:
                # delete key from dict
                del self.storage_dict[self.storage.tail.key]
                self.storage.remove_from_tail()
            # Add new item to head of linked-list
            self.storage.add_to_head(key, value)
        # Add key and value to storage_dict
            self.storage_dict[key] = self.storage.head
