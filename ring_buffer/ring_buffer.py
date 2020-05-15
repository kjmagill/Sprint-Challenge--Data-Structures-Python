from dll import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):

        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.value = item
            self.current = self.current.prev
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_item = self.storage.tail
        while current_item is not self.storage.head:
            list_buffer_contents.append(current_item.value)
            current_item = current_item.prev
        list_buffer_contents.append(self.storage.head.value)
        # print(list_buffer_contents)
        return list_buffer_contents

    # def append(self, item):
    #     # if not at capacity yet, append the item to the tail of the buffer
    #     if len(self.storage) < self.capacity:
    #         self.storage.add_to_tail(item)
            
    #         # once the first item is added, initialize self.current by setting it to the buffer's tail node
    #         if len(self.storage) == 1:
    #             self.current = self.storage.tail
    #     # otherwise, if the buffer is at max capacity
    #     else:
    #         # set the value of the current node to the new item being appended
    #         self.current.value = item
    #         # set the current node to the next. or to the head if no next exists
    #         self.current = self.current.next if self.current.next else self.storage.head

    # def get(self):
    #     # set a variable to an empty list
    #     list_buffer_contents = []
    #     # set a variable to the buffer's tail
    #     current_item = self.storage.tail

    #     # while the buffer's tail (current_item) is not the head
    #     while current_item is not self.storage.head:
    #         # append the value of the buffer's tail to the empty list created above
    #         list_buffer_contents.append(current_item.value)
    #         # iterate backwards through the list by setting the current_item to now be the tail's prev
    #         current_item = current_item.prev

    #     # append the value of the buffer's head to the list created in step-1
    #     list_buffer_contents.append(self.storage.head.value)
    #     # return the list created in step-1 once all items in the buffer have been appended to it
    #     return list_buffer_contents