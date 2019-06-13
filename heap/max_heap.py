class Heap:
    def __init__(self):
        self.storage = []

    def lemmesee(self):
        x = [str(i) for i in self.storage]
        print(x)
        return "--> ".join(x)

    def insert(self, value):
        self.storage.append(value)
        if len(self.storage) == 1:
            return
        return self._bubble_up(len(self.storage) - 1)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1)
            if self.storage[index] > self.storage[parent]:
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                    index = parent
            else:
                    break

      # insert adds the input value into the heap; this method should ensure that the
      #  inserted value is in the correct spot in the heap

      # PARENT(i) = i/2	Return the index of the father node
      # LEFT(i) = 2i	Return the index of the left child
      # RIGHT(i) = 2i+1	Return the index of the right child

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # keep bubbling up until we've either reached the top of the heap
        # or we've reached a point where the parent is higher prio
        while index > 0:
             # on a single bubble up iteration
             # get the parent index
            parent = (index - 1) // 2
            # compare the child against the value of the parent
            # if the child's value is higher prio than its parent's value
               if self.storage[index] > self.storage[parent]:
                      # swap them
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                     # update the child's index to be the new index it is now at
                    index = parent
             # otherwise, child is at a valid spot
                else:
                      # stop bubbling up
                    break

    def _sift_down(self, index):
        pass

