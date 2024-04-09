# Generator functions in Python allow you to define functions that can generate a sequence of values lazily, rather than computing them all at once and storing them in memory. This can be particularly useful when working with large datasets or when you want to iterate over a sequence of values without creating a list or tuple.
#
# The yield keyword in Python is used within generator functions to return a value to the caller and suspend the function's execution, preserving its state so that it can resume where it left off when called again. This makes it different from the return statement, which terminates the function entirely and returns a single value.

import sys


def count(num):
    count = 1
    while count <= num:
        yield count
        count += 1


for counting_num in count(10):
    print(counting_num)


# or
def count(num):
    for num in range(1, num):
        yield num


for counting_num in count(11):
    print("Size:", sys.getsizeof(counting_num))
    print(counting_num)


###########  Use of next() ##############################
def count(num):
    for num in range(1, num):
        yield num + 10


count_num = count(999000000)
print("Size:", sys.getsizeof(counting_num))
print("next", next(count_num))
print("next", next(count_num))
print("next", next(count_num))
print("next", next(count_num))
print("next", next(count_num))
print("next", next(count_num))

# Below code is not memory efficient code that's why we need genrative functions

for numb in range(1, 11):
    print(numb)
