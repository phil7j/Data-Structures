from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add to the back
        self.storage.add_to_head(value)
        self.size += 1
        return

    def dequeue(self):
        # Remove from front
        if self.len() < 1:
            return
        else:
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            self.size -= 1
            return value

    def len(self):
        return self.storage.length


# test = Queue()
# test.enqueue(5)
# test.enqueue(25)
# test.enqueue(15)
# print("Size", test.size)
# print("head", test.storage.head.value)
# print("tail", test.storage.tail.value)
# test.dequeue()
# print("Size", test.size)
# # print("Front", test.front.value)
# # print("Back", test.back.value)
# print("head", test.storage.head.value)
# print("tail", test.storage.tail.value)
