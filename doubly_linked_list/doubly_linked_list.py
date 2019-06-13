"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

         # 0 👉 1 👉 2 👉 3 👉 4 👉
    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is self.tail:
            new_head = ListNode(value)
            old_head = self.head
            self.head.prev = new_head
            self.head.next = None
            self.head = new_head
            self.head.next = old_head
            self.length += 1
        else:

            # reference to head
            old_head = self.head
        # assign new node
            new_head = ListNode(value)
        # set new node to head
            self.head = new_head
        # set old head's prev to new head
            old_head.prev = new_head
        # set new head's next to old head & prev to None
            new_head.next = old_head
        # edge cases ?
            self.length += 1

    def remove_from_head(self):
        # edge cases ?
        if self.head is self.tail:
            old_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_node.value
        else:
            # reference to old & new
            old_head = self.head
            new_head = self.head.next
        # change head reference
            self.head = new_head
        # update prev ref on new head
            self.head.prev = None
        # update next ref on old_head
            old_head.next = None
            self.length -= 1

    def add_to_tail(self, value):
        # edge cases ?
        if self.head is self.tail:
            new_tail = ListNode(value)
            self.tail = new_tail
            self.tail.prev = self.head
            self.head.next = new_tail
            self.length += 1
        else:
            # ref to old tail & new tail & old tail prev
            old_tail = self.tail
            new_tail = ListNode(value)
            old_tail_prev = self.tail.prev
            old_tail_prev.next = new_tail
            self.tail = new_tail
            self.tail.prev = old_tail_prev
            old_tail.prev = None
            old_tail.next = None
        # update old tail's prev to new tail
        # set new tail
        # set new tail prev to old tail prev
        # set old tail next/prev = None

    def remove_from_tail(self):
        #  removes the tail node and returns the value stored in it.
        if self.head is self.tail:
            old_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_node.value
        else:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None
            old_tail.next = None
            old_tail.prev = None
            self.length -= 1
            return old_tail.value

    def move_to_front(self, node):
        if self.head is self.tail:
            pass
        current = self.head
        node_to_move = None
        while current:
            if current == node:
                node_to_move = current
                node_to_update_prev = node_to_move.prev
                node_to_update_next = node_to_move.next
                node_to_update_prev.next = node_to_update_next
                node_to_update_next.prev = node_to_update_prev
                old_head = self.head
                self.head = node_to_move
                self.head.prev = None
                self.head.next = old_head
                old_head.prev = self.head
            current = current.next
        return False

    # move_to_front takes a reference to a node in the list and
    # moves it to the front of the list, shifting all other list nodes down.
    def move_to_end(self, node):
        if self.head is self.tail:
            pass
        current = self.head
        node_to_move = None
        while current:
            if current == node:
                node_to_move = current
                node_to_update_prev = node_to_move.prev
                node_to_update_next = node_to_move.next
                node_to_update_prev.next = node_to_update_next
                node_to_update_next.prev = node_to_update_prev
                old_tail = self.tail
                self.tail = node_to_move
                self.tail.prev = old_tail
                self.head.next = None
                old_tail.next = self.tail
            current = current.next
        if node_to_move is None:
            return False
        else:
            return node_to_move

    def delete(self, node):
        current = self.head
        while current:
            if current == node:
                current.delete()

    def get_max(self):
        current = self.head
        max_value = self.head.value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
