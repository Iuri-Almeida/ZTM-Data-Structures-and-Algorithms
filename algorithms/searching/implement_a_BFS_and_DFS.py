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

    def breadth_first_search(self):
        cur_node = self.root
        array = []
        queue = [cur_node]

        while len(queue) > 0:
            cur_node = queue.pop(0)  # implement a better solution
            array.append(cur_node.data)
            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

        return array

    def breadth_first_search_recursive(self, queue, array):
        if len(queue) == 0:
            return array

        cur_node = queue.pop(0)  # implement a better solution
        array.append(cur_node.data)
        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)

        return self.breadth_first_search_recursive(queue, array)

    def __traverse_in_order(self, node, arr):
        if node.left is not None:
            self.__traverse_in_order(node.left, arr)

        arr.append(node.data)

        if node.right is not None:
            self.__traverse_in_order(node.right, arr)

        return arr

    def depth_first_search_in_order(self):
        return self.__traverse_in_order(self.root, [])


my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(20)
my_tree.insert(170)
my_tree.insert(15)
my_tree.insert(1)
print(f"BFS [Iterative]: {my_tree.breadth_first_search()}")
print(f"BFS [Recursive]: {my_tree.breadth_first_search_recursive([my_tree.root], [])}")
print(f"DFS [InOrder]: {my_tree.depth_first_search_in_order()}")
