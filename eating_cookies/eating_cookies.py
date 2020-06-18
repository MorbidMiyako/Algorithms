'''
Input: an integer
Returns: an integer

initial option is plain recursion
second option is to use sets of 4

start going up from 1
after getting 3 number:
add first 3 together, set first slot
add them together again, set second slot
add together again, set third slot
ring buffer!
'''


class RingBuffer:
    def __init__(self, capacity):
        self.array = []
        self.position = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.array) < self.capacity:
            self.array.append(item)
        else:
            self.array[self.position] = item
        self.position += 1
        if self.position == self.capacity:
            self.position = 0

    def get(self):
        return self.array


def eating_cookies(n):
    total = RingBuffer(3)
    if n == 0:
        return 1
    total.append(1)
    n -= 1
    while n > 0:
        total.append(sum(total.array))
        n -= 1
    return sum(total.array)

    # # Your code here
    # # memory:
    # if n >4
    # slot_1 = [x]
    # slot_2 = [x]

    # ways = 0
    # if n >= 3:
    #     ways += eating_cookies(n - 3)
    # if n >= 2:
    #     ways += eating_cookies(n - 2)
    # if n >= 1:
    #     ways += eating_cookies(n - 1)
    # return ways
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    # num_cookies = 5

    # print(
    #     f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    for i in range(0, 10):
        print(eating_cookies(i))

"""
if n
n -1
n -2 n -2
n -3 n -3 n -3 n -3
     n -4 n -4 n -4 n -4 n-4 n -4 n -4
          n -5 n -5 n -5 n-5 n -5 n -5 n -5 n -5 n -5 n -5 n -5 n -5 n -5
                    n -6 n-6 n -6 n -6 n -6 n -6 n -6 n -6 n -6 n -6 n -6 n -6 *13
                                       n -7

1
2
4
"""
