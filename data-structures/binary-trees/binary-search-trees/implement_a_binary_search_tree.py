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

        # right child
        if node.data > prev_node.data:
            # with right child
            if node.right is not None:
                node_right = node.right
                while node_right.left is not None and node_right.left.left is not None:
                    node_right = node_right.left
                # right child with no left child
                if node_right.left is None:
                    prev_node.right = node_right
                    node_right.left = node.left
                # right child with left child
                else:
                    prev_node.right = node_right.left  # first
                    node_right.left.left = node.left  # second
                    node_right.left = node_right.left.right  # third
                    prev_node.right.right = node.right  # fourth
            # no right child
            else:
                prev_node.right = node.left
        # left child
        else:
            # with right child
            if node.right is not None:
                node_right = node.right
                while node_right.left is not None and node_right.left.left is not None:
                    node_right = node_right.left
                # right child with no left child
                if node_right.left is None:
                    prev_node.left = node_right
                    node_right.left = node.left
                # right child with left child
                else:
                    prev_node.left = node_right.left  # first
                    node_right.left.left = node.left  # second
                    node_right.left = node_right.left.right  # third
                    prev_node.left.right = node.right  # fourth
            # no right child
            else:
                prev_node.left = node.left
        return node.data


my_tree = BinarySearchTree()

# testing left side
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
print(f"Removed: {my_tree.remove(20)}")
print(f"Removed: {my_tree.remove(25)}")
print(f"Root [41]: {my_tree.root.data}")
print(f"Root-Left [21]: {my_tree.root.left.data}")
print(f"Root-Left-Left [11]: {my_tree.root.left.left.data}")
print(f"Root-Left-Right [29]: {my_tree.root.left.right.data}")
print(f"Root-Left-Right-Right [32]: {my_tree.root.left.right.right.data}")
print(f"Root-Left-Right-Left [28]: {my_tree.root.left.right.left.data}")
print(f"Root-Left-Right-Left-Right [None]: {my_tree.root.left.right.left.right}")
print(f"Root-Left-Right-Left-Left [24]: {my_tree.root.left.right.left.left.data}")
print(f"Root-Left-Right-Left-Left-Left [22]: {my_tree.root.left.right.left.left.left.data}")
print(f"Root-Left-Right-Left-Left-Left-Right [23]: {my_tree.root.left.right.left.left.left.right.data}")
print(f"Root-Left-Right-Left-Left-Left-Left [None]: {my_tree.root.left.right.left.left.left.left}")
# print(f"Root-Left-Right-Left-Left-Left-Left-Right [None]: {my_tree.root.left.right.left.left.left.left.right}")
# print(f"Root-Left-Right-Left-Left-Left-Left-Left [None]: {my_tree.root.left.right.left.left.left.left.left}")

print("-" * 30)

# testing right side
# my_tree.insert(41)
my_tree.insert(70)
my_tree.insert(52)
my_tree.insert(90)
my_tree.insert(92)
my_tree.insert(78)
my_tree.insert(84)
my_tree.insert(74)
my_tree.insert(72)
my_tree.insert(73)
my_tree.insert(71)
print(f"Removed: {my_tree.remove(70)}")
print(f"Removed: {my_tree.remove(78)}")
print(f"Root [41]: {my_tree.root.data}")
print(f"Root-Right [71]: {my_tree.root.right.data}")
print(f"Root-Right-Left [52]: {my_tree.root.right.left.data}")
print(f"Root-Right-Right [90]: {my_tree.root.right.right.data}")
print(f"Root-Right-Right-Right [92]: {my_tree.root.right.right.right.data}")
print(f"Root-Right-Right-Left [84]: {my_tree.root.right.right.left.data}")
print(f"Root-Right-Right-Left-Right [None]: {my_tree.root.right.right.left.right}")
print(f"Root-Right-Right-Left-Left [74]: {my_tree.root.right.right.left.left.data}")
print(f"Root-Right-Right-Left-Left-Right [None]: {my_tree.root.right.right.left.left.right}")
print(f"Root-Right-Right-Left-Left-Left [72]: {my_tree.root.right.right.left.left.left.data}")
print(f"Root-Right-Right-Left-Left-Left-Right [73]: {my_tree.root.right.right.left.left.left.right.data}")
print(f"Root-Right-Right-Left-Left-Left-Left [None]: {my_tree.root.right.right.left.left.left.left}")
# print(f"Root-Right-Right-Left-Left-Left-Left-Right [None]: {my_tree.root.right.right.left.left.left.left.right}")
# print(f"Root-Right-Right-Left-Left-Left-Left-Left [None]: {my_tree.root.right.right.left.left.left.left.left}")
