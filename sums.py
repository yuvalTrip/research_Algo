import heapq
from heapq import heappop, heappush
from itertools import takewhile, islice

def sorted_subset_sums(S):
    """
    Yield all subset sums of a series S in ascending order.

    >>> from itertools import takewhile, islice
    >>> for i in sorted_subset_sums([1,2,4]): print(i, end=", ")
    0, 1, 2, 3, 4, 5, 6, 7,

    >>> list(sorted_subset_sums([1,2,3]))
    [0, 1, 2, 3, 3, 4, 5, 6]

    >>> list(sorted_subset_sums([2,3,4]))
    [0, 2, 3, 4, 5, 6, 7, 9]

    >>> list(islice(sorted_subset_sums(range(100)),5))
    [0, 0, 1, 1, 2]

    >>> list(takewhile(lambda x:x<=6, sorted_subset_sums(range(1,100))))
    [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6]

    >>> list(zip(range(5), sorted_subset_sums(range(100))))
    [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2)]

    >>> len(list(takewhile(lambda x:x<=1000, sorted_subset_sums(list(range(90,100)) + list(range(920,1000))))))
    1104
    """
    # Sort the input series
    S = sorted(S)
    # Length of the series
    n = len(S)
    # Initialize a min-heap with a tuple (current_sum, index_in_S)
    heap = [(0, -1)]  # (current_sum, index_in_S)
    # A set to track visited states to avoid duplicates
    seen = set(heap)

    # Continue until the heap is empty
    while heap:
        # Pop the smallest current sum and its index from the heap
        current_sum, idx = heappop(heap)
        # Yield the current sum
        yield current_sum

        # Iterate over the remaining elements in S
        for next_idx in range(idx + 1, n):
            # Calculate the new sum by adding the next element
            new_sum = current_sum + S[next_idx]
            # Create a new state tuple (new_sum, next_idx)
            new_state = (new_sum, next_idx)
            # If the new state is not visited yet
            if new_state not in seen:
                # Push the new state onto the heap
                heappush(heap, new_state)
                # Add the new state to the seen set
                seen.add(new_state)
                # Remove the previous occurrences of new_sum from the seen set
                for s in list(seen):
                    if s[0] == new_sum:
                        seen.remove(s)
# Doctests
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    for i in eval(input()):
        print(i, end=", ")

# Example usage:
# from itertools import takewhile, islice
# print(list(sorted_subset_sums([1, 2, 4])))
# print(list(sorted_subset_sums([1, 2, 3])))
# print(list(sorted_subset_sums([2, 3, 4])))
# print(list(islice(sorted_subset_sums(range(100)), 5)))
# print(list(takewhile(lambda x: x <= 6, sorted_subset_sums(range(1, 100)))))
# print(list(zip(range(5), sorted_subset_sums(range(100)))))
# print(len(list(takewhile(lambda x: x <= 1000, sorted_subset_sums(list(range(90, 100)) + list(range(920, 1000)))))))
