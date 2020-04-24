from doubly_linked_list import DoublyLinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()

#     def append(self, item):
#         if len(self.storage) == self.capacity:
#             self.current = 0

#     def get(self):
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []

#         # TODO: Your code here
#         return self.storage
#         return list_buffer_contents

# --------------------------------------------------------------

# class RingBuffer:
#     """ class that implements a not-yet-full buffer """
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()

#         def append(self, item):
#             """ Append an element overwriting the oldest one. """
#             self.storage[self.current] = item
#             self.current = (self.current+1) % self.capacity
#             self.storage.

#             if self.storage.length() == self.capacity:
#                 self.current = 0
#         def get(self):
#             """ return list of elements in correct order """
#             list_buffer_contents = [] 
#             return list_buffer_contents

# ---------------------------------------------------------------

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            node = self.storage.head

            if self.current == self.capacity:
                self.current = 0

            for x in range(0, self.current):
                node = node.next

            node.value = item
            self.current += 1

        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        first = self.storage.head

        while first:
            list_buffer_contents.append(first.value)
            first = first.next
        return list_buffer_contents







# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
