class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # The reverse_list() method 
    def reverse_list(self, node, prev):
        # create a previous_node variable to represent the former head node, and set its initial value to None
        previous_node = None
        # create a current_head variable to represent the current head position in the linked list
        current_head = self.head
        # while a head node exists in the linked list
        while current_head is not None:
            # create a next_up variable to represent the current head's next node
            next_up = current_head.next_node
            # update the current head's next node to be the previous_node variable
            current_head.next_node = previous_node
            # set the previous_node variable to be the current head
            previous_node = current_head
            # set the new head node to be the current head's next node
            current_head = next_up
        # set the new head node to now be the previous_node variable (either the former head or None)
        self.head = previous_node