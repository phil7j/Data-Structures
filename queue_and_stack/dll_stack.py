from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Add to the Top
        self.storage.add_to_head(value)
        self.size += 1
        return

    def pop(self):
        # Remove from top
        if self.len() < 1:
            return
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return value

    def len(self):
        return self.storage.length
