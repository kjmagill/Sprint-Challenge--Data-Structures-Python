from dll import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # Had to add this __iter__ method to allow the RingBuffer object to be iterable
    # This resolves the bug I was experiencing when attempting to iterate over 'self' in the get() method to pull items into a list
    def __iter__(self):
        # create a {current} variable to represent the head of the buffer
        current = self.storage.head
        # while a head node exists in the buffer
        while current:
            # create an {item} variable set to the current head of the buffer
            item = current
            # update the {current} variable to now be the head's next node in the buffer
            current = current.next
            # yield the value of the former head of the buffer
            yield item.value

    def append(self, item):
        # if not at capacity yet, append the item to the tail of the buffer
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

            # once the first item is added, initialize self.current by setting it to the buffer's tail node
            if len(self.storage) == 1:
                self.current = self.storage.tail
        else:
            # otherwise, if the buffer is at max capacity then set the value of the current node to the new item being appended
            self.current.value = item
            # set the current node to the next. or to the head if no next exists
            self.current = self.current.next if self.current.next else self.storage.head

    def get(self):
        # create a list by iterating through the DLL for items
        list_buffer_contents = [item for item in self if not None]

        # return the list created in step-1 once all items in the buffer have been appended to it
        return list_buffer_contents