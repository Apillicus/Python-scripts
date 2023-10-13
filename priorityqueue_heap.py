
import simple_array
import logging

logging.basicConfig(level=logging.DEBUG)

INITIAL_CAPACITY = 10

class PriorityQueue:

    def _left_index(index):
        return 2 * index + 1

    def _right_index(index):
        return 2 * index + 2

    def _parent_index(index):
        return (index-1)//2

    def __init__(self):
        self.array = simple_array.SimpleArray(INITIAL_CAPACITY)
        self.logical_size = 0

    def is_empty(self):
        return self.logical_size == 0

    def __len__(self):
        return self.logical_size

    def peek(self):
        if self.logical_size == 0:
            raise EmptyQueue("Can't peek in an empty queue.")
        return self.array[0]

    def enqueue(self,value):

        self._grow_if_necessary()

        self.array[self.logical_size] = value
        self.logical_size += 1

        self._bubble_up(self.logical_size-1)

    def _bubble_up(self,index):
        # if i'm NOT root
        if index != 0:
            parent_index = PriorityQueue._parent_index(index)
            logging.debug(f"Comparing node {index} to node {parent_index}")
            # if i'm strictly smaller than parent
            if self.array[index] < self.array[parent_index]:
                # swap values
                temp = self.array[index]
                self.array[index] = self.array[parent_index]
                self.array[parent_index] = temp
                self._bubble_up(parent_index)

    def _capacity(self):
        return len(self.array)

    def _grow_if_necessary(self):

        if self._capacity() == self.logical_size:
            new_array = simpleArray.SimpleArray(self._capacity()*2)
            for i in range(self.logical_size):
                new_array[i] = self.array[i]
            self.array = new_array

class EmptyQueue(Exception):
    pass

if __name__ == "__main__":
    pq = PriorityQueue()
    for val in [5,7,3,2]:
        pq.enqueue(val)
        print(pq.peek())
        print(pq.array)
        print()
