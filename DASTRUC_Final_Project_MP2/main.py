class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.sibling = None
        self.degree = 0
        self.depth = 0


class BinarySearchTree:
    """A class representing a binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new node with the given value in the proper position in the tree."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            parent_node = None
            while current_node:
                parent_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            if value < parent_node.value:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            new_node.parent = parent_node

    def pre_order_traversal(self):
        """Print the values of the nodes in pre-order traversal order."""
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, current_node):
        if current_node is None:
            return
        print(current_node.value, end=" ")
        self._pre_order_traversal(current_node.left)
        self._pre_order_traversal(current_node.right)

    def post_order_traversal(self):
        """Print the values of the nodes in post-order traversal order."""
        self._post_order_traversal(self.root)

    def _post_order_traversal(self, current_node):
        if current_node is None:
            return
        self._post_order_traversal(current_node.left)
        self._post_order_traversal(current_node.right)
        print(current_node.value, end=" ")

    def in_order_traversal(self):
        """Print the values of the nodes in in-order traversal order."""
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        if current_node is None:
            return
        self._in_order_traversal(current_node.left)
        print(current_node.value, end=" ")
        self._in_order_traversal(current_node.right)

    def get_node_info(self):
        """Yield a tuple of node information for each node in the tree.
        Node information includes: value, parent node, sibling node, left child node,
        right child node, degree (number of children), and depth.
        """
        if self.root is None:
            print("Error: The tree is empty.")
            return
        else:
            yield from self._get_node_info(self.root)

    def _get_node_info(self, current_node):
        if current_node.left is not None:
            yield from self._get_node_info(current_node.left)
        if current_node.parent:
            if current_node is current_node.parent.left:
                current_node.sibling = current_node.parent.right
            else:
                current_node.sibling = current_node.parent.left
            current_node.degree = sum([current_node.left is not None, current_node.right is not None])
            current_node.depth = self.get_node_depth(current_node)
            yield (
                current_node.value,
                current_node.parent.value if current_node.parent else "NULL",
                current_node.sibling.value if current_node.sibling else "NULL",
                current_node.left.value if current_node.left else "NULL",
                current_node.right.value if current_node.right else "NULL",
                current_node.degree,
                current_node.depth,
            )
        if current_node.right is not None:
            yield from self._get_node_info(current_node.right)

    def get_node_depth(self, current_node, depth=0):
        """Return the depth of the given node."""
        if current_node.parent is None:
            return depth
        else:
            return self.get_node_depth(current_node.parent, depth + 1)


def main():
    try:
        filename = input("Input the name and extension of the file: ")
        with open(filename, "r") as f:
            data = f.readlines()
        bst = BinarySearchTree()
        for value in data:
            bst.insert(int(value.strip()))  # Modified to strip leading/trailing whitespaces

        print("Pre-order traversal:")
        bst.pre_order_traversal()
        print()

        print("Post-order traversal:")
        bst.post_order_traversal()
        print()

        print("In-order traversal:")
        bst.in_order_traversal()
        print()

        print("Node Parent Sibling Left Child Right Child Degree Depth")
        for node_info in bst.get_node_info():
            print(
                f"{node_info[0]:<5} {node_info[1]:<7} {node_info[2]:<8} "
                f"{node_info[3]:<11} {node_info[4]:<12} {node_info[5]:<7} {node_info[6]:<5}"
            )

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid input in file.")


if __name__ == "__main__":
    main()
