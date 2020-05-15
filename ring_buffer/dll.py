"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after the current node."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before the current node."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges the current ListNode's previous and next pointers
    accordingly, effectively deleting the ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""The doubly-linked list (DLL) class holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the DLL."""
    def add_to_head(self, value):
        # create a new ListNode with the passed-in value, and increment the current length of the DLL by 1
        new_node = ListNode(value, None, None)
        self.length += 1

        # if the DLL is empty, set the current head and tail nodes to the new ListNode
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new ListNode's next node to the current head
            new_node.next = self.head
            # set the current head's prev node to the new ListNode
            self.head.prev = new_node
            # set the current head to be the new ListNode
            self.head = new_node

    """Removes the DLL's current head node, making the
    current head's next node the new head of the DLL."""
    def remove_from_head(self):
        # set a variable to the value of the current head node
        value = self.head.value
        # delete the current head node from the DLL
        self.delete(self.head)
        # return the value of the removed node
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the DLL."""
    def add_to_tail(self, value):
        # create a new ListNode with the passed-in value, and increment the DLL's length by 1
        new_node = ListNode(value, None, None)
        self.length += 1

        # if the DLL is empty, set the current head and tail nodes to the new ListNode
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new ListNode's prev node to the current tail
            new_node.prev = self.tail
            # set the current tail's next node to the new ListNode
            self.tail.next = new_node
            # set the current tail to be the new ListNode
            self.tail = new_node

    """Removes the DLL's current tail, making the 
    current tail's previous node the new tail node."""
    def remove_from_tail(self):
        # set a variable to the value of the current tail node
        value = self.tail.value
        # delete the current tail node from the DLL
        self.delete(self.tail)
        # return the value of the removed node
        return value

    """Removes the input node from its current spot in the 
    DLL and inserts it as the new head node."""
    def move_to_front(self, node):
        # if this node is the current head, do nothing and move on
        if node is self.head:
            return

        # set a variable to the value of this node
        value = node.value

        # if this node is the current tail, remove it from the tail
        if node is self.tail:
            self.remove_from_tail()
        # otherwise, delete this node and decrement the DLL's length by 1
        else:
            node.delete()
            self.length -= 1

        # lastly, add this node as the current head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    DLL and inserts it as the new tail node."""
    def move_to_end(self, node):
        # if this node is the current tail, then do nothing and move on
        if node is self.tail:
            return

        # create a variable set to the value of this node
        value = node.value

        # if this node is the current head, remove it from the head
        if node is self.head:
            self.remove_from_head()
        # otherwise, delete this node and decrement the DLL's length by 1
        else:
            node.delete()
            self.length -= 1

        # lastly, add this node as the current tail
        self.add_to_tail(value)

    """Removes a node from the DLL and handles cases where
    the node was the head or the tail."""
    def delete(self, node):
        # decrement the DLL's length by 1
        self.length -= 1

        # if the DLL is empty, do nothing and move on
        if not self.head and not self.tail:
            return

        # if the DLL contains only this node, set the current head and tail to None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # else, if this node is the current head, set the current head to this node's next node then delete this node
        elif self.head == node:
            self.head = node.next
            node.delete()
        # else, if this node is the current tail, set the current tail to this node's prev node then delete this node
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        # otherwise, simply delete this node
        else:
            node.delete()
        
    """Returns the highest value currently in the DLL."""
    def get_max(self):
        # if the DLL is empty, return None
        if not self.head and not self.tail:
            return None
        # create a variable to represent the max_value and set it to the value of the current head node
        max_value = self.head.value
        # set a variable to the current head position in the DLL
        current_head = self.head
        # while a head node exists in the DLL
        while current_head:
            # if the current head node's value is greater than the last head node's value
            if current_head.value > max_value:
                # update the max_value variable to now be the new head node's value
                max_value = current_head.value
            # then move on to the next node in the DLL by setting the new head to be the current head's next node
            current_head = current_head.next
        # return the max value for all nodes in the DLL
        return max_value
