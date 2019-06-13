class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

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
        # check if the new node's value is less than our current node's value
    if value < self.value:
        # if there's no left child here already, place the new node here
        if not self.left:
            self.left = BinarySearchTree(new_tree)
        else:
            # otherwise, repeat the process!
            self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
        # if there's no right child here already, place the new node here
        if not self.right:
            self.right = BinarySearchTree(new_tree)
        else:
            # otherwise, repeat the process!
            self.right.insert(value)

    #     # adds the input value to the binary search tree,
    #     # adhering to the rules of the ordering of elements in a binary search tree.

        def contains(self, target):
            if self.left is None and self.right is None:
                return False
            if target == self.value:
                return True
            if target > self.value:
                if self.right:
                    self = self.right
                    return self.contains(target)
                else:
                    return False
            elif target < self.value:
                if self.left:
                    self = self.left
                    return self.contains(target)
                else:
                    return False

    #     # searches the binary search tree for the input value,
    #     # returning a boolean indicating whether the value exists in the tree or not.

    def get_max(self):
            # returns the maximum value in the binary search tree.
            # if possible go right if not return root
            # traverse right until None is reached and then return
        if self.right is None:
            return self.value
        while self.right:
            self = self.right
        return self.value

    def for_each(self, cb):
        # performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value.
        # There is a myriad of ways to perform tree traversal; in this case any of them should work.
        # use queue to store nodes
        # perform cb on each value
        for_each_queue = [self]
        while for_each_queue:
            item = for_each_queue.pop(0)
            new_val = cb(item.value)
            item.value = new_val
            if item.left:
                for_each_queue.append(item.left)
            if item.right:
                for_each_queue.append(item.right)
    #     example cb for for_each method
    #     def add_5(val):
    #       val = val + 5
    #       return val
