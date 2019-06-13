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

    def delete(self):
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        start = 0
        while start <= len(self.storage) - 3:
          ind = max(self.storage[start + 1], self.storage[start + 2])
          index = self.storage.index(ind)
          start += 1
          self._bubble_up(index)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

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
      left = self.storage[2 * index]
      right = self.storage[(2 * index) + 1]
      max_val = max(left, right)
      if self.storage[index] < max_val:
        swap_index = self.storage.index(max_val)
        val = self.storage[index]
        self.storage[index] = max_val
        self.storage[swap_index] = val
      


