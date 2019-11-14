import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if value is bigger or smaller than current node value
        # if bigger, if self.right = None, then insert node there, make current_node, self.right
        # if smaller, if self.right = None, then insert node there, make current_node, self.left
        current = self
        new_node = BinarySearchTree(value)
        # print("LEFT AND RIGHT NODES",current.left, current.right)
        while current.left != None or current.right != None:
            # print("In Loops")
            if current.value <= value:
                if current.right == None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            elif current.value > value:
                if current.left == None:
                    current.left = new_node
                    return
                else:
                    current = current.left
        #otherwise if current.left and current.right ARE None
        if value >= current.value:
            # print("No nodes and bigger then root")
            current.right = new_node
            return
        else:
            # print("No Nodes, and smaller then Root")
            current.left = new_node
            return



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #To search a given key in Binary Search Tree, we first compare it with root,
        # if the key is present at root, we return root. If key is greater than root's key,
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        current = self
        # print("LEFT AND RIGHT NODES",current.left, current.right)
        while current.left != None or current.right != None:
            # print("In Loops")
            if current.value == target:
                return True
            elif target > current.value:
                current = current.right
                continue
            elif target < current.value:
                current = current.left
                continue
        #otherwise if current.left and current.right ARE None
        if target == current.value:

            return True
        else:

            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go right no further
        current = self

        while current.right:
        # Keep going right
            if current.right == None:
                return current.value
            else:
                current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(2)
bst.insert(3)
bst.insert(7)
# bst.insert(6)

print(bst.contains(7))