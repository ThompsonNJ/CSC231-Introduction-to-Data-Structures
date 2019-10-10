import time
import random


# a is a list of objects.
# n is the number of elements in a.
# target is the item for which to search. It has the same type as an element of a.
# this function returns a tuple:
#   the first element is the index of the target in the list or None if not found
#   the second element is the number of comparisons required to determine the target's index
def sequential_search(a, target):
    comparisons = 0
    pos = 0
    done = False
    while pos < len(a) and not done:
        comparisons += 1
        if target == a[pos]:
            done = True
        else:
            pos += 1

    if pos == len(a):
        pos = None

    return pos, comparisons


# a is a list of objects and the elements a[0] – a[n-1] are in ascending order.
# n is the number of elements in a.
# target is the item for which to search. It has the same type as an element of a.
# this function returns a tuple:
#   the first element is the index of the target in the list or None if not found
#   the second element is the number of comparisons required to determine the target's index
def smart_sequential_search(a, target):
    comparisons = 0
    pos = 0
    done = False
    while pos < len(a) and not done:
        comparisons += 1
        if target <= a[pos]:
            done = True
        else:
            pos += 1

    if pos == len(a) or target != a[pos]:
        pos = None

    return pos, comparisons


# a is a list of objects and the elements a[0] – a[n-1] are in ascending order.
# n is the number of elements in a.
# target is the item for which to search. It has the same type as an element of a.
# this function returns a tuple:
#   the first element is the index of the target in the list or None if not found
#   the second element is the number of comparisons required to determine the target's index
def binary_search(a, target):
    comparisons = 0
    found = False
    first = 0
    last = len(a) - 1

    while first <= last and not found:
        mid = (first + last) // 2
        comparisons += 1
        if target < a[mid]:
            last = mid - 1
        elif target > a[mid]:
            first = mid + 1
        else:
            found = True

    if not found:
        mid = None

    return mid, comparisons


# This program runs experiments that test the performance of search algorithms.
if __name__ == '__main__':
    num_to_generate = max_range = 1000000      # Change this value
    num_searches = 1000

    nums = [random.randint(0, max_range) for i in range(num_to_generate)]

    print('Starting experiment. Performing searches of {} random numbers on a list of size {}...'.format(num_searches, num_to_generate))

    start = time.time()
    seq_total = 0
    for i in range(num_searches):
        target = random.randint(0, 5000)
        index, comps = sequential_search(nums, target)
        seq_total += comps

    print('Sequential search:\n\ttime taken={:.3f}s\n\taverage # of comparisons={}'.format(time.time() - start, seq_total // num_searches))

    start = time.time()
    nums.sort()
    time_to_sort = time.time()-start
    print("Time to sort the list of {} random numbers: {:.3f}s".format(num_to_generate, time_to_sort))

    start = time.time()
    smart_seq_total = 0
    for i in range(num_searches):
        target = random.randint(0, 5000)
        index, comps = smart_sequential_search(nums, target)
        smart_seq_total += comps

    print('Smart sequential search:\n\ttime taken={:.3f}s\n\taverage # of comparisons={}'.format(time.time() - start + time_to_sort,
                                                                                      smart_seq_total // num_searches))

    start = time.time()
    bin_total = 0
    for i in range(num_searches):
        target = random.randint(0, 5000)
        index, comps = binary_search(nums, target)
        bin_total += comps

    print('Binary search:\n\ttime taken={:.3f}s\n\taverage # of comparisons={}'.format(time.time() - start + time_to_sort,
                                                                                      bin_total // num_searches))
