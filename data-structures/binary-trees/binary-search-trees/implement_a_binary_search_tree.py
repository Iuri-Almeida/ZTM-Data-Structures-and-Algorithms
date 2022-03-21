class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return self.data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search_node(self, value):
        node = prev_node = self.root
        while node is not None:
            if value > node.data:
                prev_node = node
                node = node.right
            elif value < node.data:
                prev_node = node
                node = node.left
            else:
                return prev_node, node
        return prev_node, node

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if value > node.data:
                    if node.right is None:
                        node.right = new_node
                        break
                    node = node.right
                elif value < node.data:
                    if node.left is None:
                        node.left = new_node
                        break
                    node = node.left
                else:
                    raise ValueError("No duplicated values allowed!")

    def lookup(self, value):
        if self.root is None:
            raise ReferenceError("Tree is empty! There is no root node.")

        node = self.root
        while node is not None:
            if value > node.data:
                node = node.right
            elif value < node.data:
                node = node.left
            else:
                return node.data
        return None

    def remove(self, value):
        if self.root is None:
            raise ReferenceError("Tree already empty! You can't remove from nothing.")

        # reference the node that we're looking for and the previous one
        prev_node, node = self.__search_node(value)
        if node is None:
            raise IndexError(f"Could not find the value = {value}")

        # if it's on the right side
        if node.data > prev_node.data:
            if node.right is not None:
                node_right = node.right
                while node_right.left is not None and node_right.left.left is not None:
                    node_right = node_right.left
                if node_right.left is None:
                    prev_node.right = node_right
                    node_right.left = node.left
                else:
                    prev_node.right = node_right.left
                    node_right.left = node_right.left.right
                    node_right.left.left = node.left
                    node_right.left.right = node.right
            else:
                prev_node.right = node.left
        else:
            if node.right is not None:
                node_right = node.right
                while node_right.left is not None and node_right.left.left is not None:
                    node_right = node_right.left
                if node_right.left is None:
                    prev_node.left = node_right
                    node_right.left = node.left
                else:
                    prev_node.left = node_right.left
                    node_right.left = node_right.left.right
                    node_right.left.left = node.left
                    node_right.left.right = node.right
            else:
                prev_node.left = node.left
        return node.data


my_tree = BinarySearchTree()
my_tree.insert(41)
my_tree.insert(20)
my_tree.insert(29)
my_tree.insert(11)
my_tree.insert(32)
my_tree.insert(25)
my_tree.insert(28)
my_tree.insert(24)
my_tree.insert(22)
my_tree.insert(23)
my_tree.insert(21)
# print(my_tree.lookup(2092))
print(my_tree.remove(20))
print(f"Root-Left [21]: {my_tree.root.left.data}")
print(f"Root-Left-Left [11]: {my_tree.root.left.left.data}")
print(f"Root-Left-Right [29]: {my_tree.root.left.right.data}")
print(f"Root-Left-Right-Left-Left-Left [22]: {my_tree.root.left.right.left.left.left.data}")
print(f"Root-Left-Right-Left-Left-Left [None]: {my_tree.root.left.right.left.left.left}")

