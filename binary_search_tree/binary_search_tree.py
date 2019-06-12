class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

# .     8
    #   3 .    10 .        #11 .      7
        #   3 .    10
        #          9   11
    # 1   6 .     14
    #    4 . 7 . 13

    def print_tree(self):
        nodes = []
        left_nodes = []
        while self.right or self.left:
            if self.left:
                left_nodes.append(str(self.left.value))
                self.left = self.left.left
            if self.right:
                if self.right.value == 12:
                    print(self.right.left)
                    print(self.right.right.value)
                nodes.append(str(self.right.value))
                self.right = self.right.right
        return f"{left_nodes} ~~~ {nodes}"
        return "->".join(nodes)

    def insert(self, value):
        node = BinarySearchTree(value)
        if self.left is None and node.value < self.value:
            self.left = node
            return node
        if self.right is None and node.value > self.value:
            self.right = node
            return node
        nodes_to_visit = []
        lower_bound = None
        upper_bound = None
        if node.value > self.value:
            nodes_to_visit.append(self.right)
            lower_bound = self.value
            upper_bound = 999999
        else:
            nodes_to_visit.append(self.right)
            lower_bound = -99999
            upper_bound = self.value
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            if current_node.value > node.value and current_node.left is None:
                current_node.left = node
                # print(f"node placed at {current_node.value}")
                break
            elif current_node.value < node.value and current_node.right is None:
                current_node.right = node
                # print(f"node placed at {current_node.value}")
                break

            if current_node.value < node.value:
                nodes_to_visit.append(current_node.right)
                lower_bound = current_node.value

    #     # adds the input value to the binary search tree,
    #     # adhering to the rules of the ordering of elements in a binary search tree.

    # def contains(self, target):
    #     # searches the binary search tree for the input value,
    #     # returning a boolean indicating whether the value exists in the tree or not.

    # def get_max(self):
    #     # returns the maximum value in the binary search tree.

    # def for_each(self, cb):
        # performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value.
        # There is a myriad of ways to perform tree traversal; in this case any of them should work.
