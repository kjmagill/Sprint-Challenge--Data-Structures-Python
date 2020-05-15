class BSTNode:
    def __init__(self, value): # each node's key is its value
        self.value = value
        self.left = None
        self.right = None

    # The insert() method inserts the given value into the tree
    def insert(self, value):
        done = False
        # create a variable called current and set it equal to the current node in the tree
        current = self
        # work through the tree, checking if the new value is greater than or less than each current node's value
        while done == False:
            # if the new value is less than the current node's value...
            if value < current.value:
                # if the current node has no left node, then...
                if current.left is None:
                    # create a new BSTNode and pass in the value
                    bst = BSTNode(value)
                    # set the new BSTNode to the current node's left node
                    current.left = bst
                    # set done equal to True, which stops looping through the tree and completes the insert() method
                    done = True
                # otherwise
                else:
                    # set the variable { current } to be the current node's left node, then repeat the insert() method
                    current = current.left
            # otherwise
            else:
                # if the current node has no right node, then...
                if current.right is None:
                    # create a new BSTNode and pass in the value
                    bst = BSTNode(value)
                    # set the new BSTNode to the current node's right node
                    current.right = bst
                    # set done equal to True, which stops looping through the tree and completes the insert() method
                    done = True
                # otherwise
                else:
                    # set the variable { current } to be the current node's right node, then repeat the insert() method
                    current = current.right

    # The contain() method returns True if the tree contains the value, or False if it does not
    def contains(self, target):
        done = False
        # create a variable called current and set it equal to the current node in the tree
        current = self
        # work through the tree, checking to see if the target value is contained in any current node's value
        while done == False:
            # if the current node's value is equal to the target value, then...
            if current.value == target:
                # return True and complete the contains() method
                return True
            # else, if the current node has no left node and no right node, then...
            elif current.left is None and current.right is None:
                # return False and complete the contains() method
                return False
            # else, if the target value is less than the current node's value, then...
            elif target < current.value:
                # set the variable { current } to be the current node's left node, then repeat the contains() method
                current = current.left
            # otherwise
            else:
                # set the variable { current } to be the current node's right node, then repeat the contains() method
                current = current.right

    # The get_max() method returns the maximum value found in the tree
    def get_max(self):
        done = False
        # create a variable called current and set it equal to the current node in the tree
        current = self
        # work through the tree until finding the node with the max value
        while done == False:
            # if the current node has no right node, then...
            if current.right is None:
                # return the current node's value (this is the max value in the tree!)
                return current.value
            # otherwise
            else:
                # set the variable { current } to be the current node's right node, then repeat the get_max() method
                current = current.right

    # The for_each() method calls a specific function (fn) on the value of each node
    def for_each(self, fn):
        # create a variable called current and set it equal to the current node in the tree
        current = self
        # execute the passed-in function using the current node's value
        fn(current.value)
        # if the current node has a right node, then...
        if current.right:
            # execute the passed-in function for each of the current node's right nodes
            current.right.for_each(fn)
        # if the current node has a left node, then...
        if current.left:
            # execute the passed-in function for each of the current node's left nodes
            current.left.for_each(fn)