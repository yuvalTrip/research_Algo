"""
A TSP algorithm usually creates a list of the shortest paths.

A 'dist_mat' is a class that manages a matrix of distances.
It creates a new track.

It uses the FlyWeight design pattern. See: https://refactoring.guru/design-patterns/flyweight

Author: Yuval Ben Simhon
Since:  2024-05
"""

from abc import ABC, abstractmethod

import numpy as np, itertools
from typing import Any, Callable, List, Tuple, Iterator

Track=List

def track2str(track: Track) -> str:
    # Track is a list (of cities or indices of cities) i.e [0, 1, 3, 2, 0] or ['A', 'B', 'D', 'C', 'A']:
    return f"Track: {', '.join(track)}"


def printbins(track: Track):
    print(track2str(track))


class Track(ABC):
    """
    An abstract track-list manager.

    All arrays created by the same binner share the following two variables:
     * numbins - the total number of bins.
     * valueof - a function that maps an item to its value.
    """

    def __init__(self, valueof: Callable = lambda x: x):
        self.valueof = valueof

    @abstractmethod
    def new_track(self) -> Track:
        '''
        Create a new track.
        '''
        return None

    @abstractmethod
    def add_item_to_track(self, bins: Track, item: Any, track_index: int) -> Track:
        """
        Add the given item to the given bin in the given array.
        Return the bins after the addition.
        """
        return bins

    @abstractmethod
    def sums(self, bins: Track) -> Tuple[float]:
        """
        Return only the current sums.
        """
        return None


class BinnerKeepingSums(Binner):
    """
    A binner that creates bin-arrays that keep track only of the total sum in each bin.

    >>> values = {"a":3, "b":4, "c":5, "d":5, "e":5}
    >>> binner = BinnerKeepingSums(lambda x: values[x])
    >>> bins = binner.new_bins(3)
    >>> printbins(binner.add_item_to_bin(bins, item="a", bin_index=0))
    Bin #0: sum=3.0
    Bin #1: sum=0.0
    Bin #2: sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="b", bin_index=1)
    >>> printbins(bins)
    Bin #0: sum=3.0
    Bin #1: sum=4.0
    Bin #2: sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="c", bin_index=1)
    >>> printbins(bins)
    Bin #0: sum=3.0
    Bin #1: sum=9.0
    Bin #2: sum=0.0
    """

    def __init__(self, valueof: Callable = lambda x: x):
        super().__init__(valueof)

    BinsArray = np.ndarray  # Here, the bins-array is simply an array of the sums.

    def new_bins(self, numbins) -> BinsArray:
        bins = np.zeros(numbins)  # similar to numbins*[0]
        return bins

    def add_item_to_bin(self, bins: BinsArray, item: Any, bin_index: int) -> BinsArray:
        bins[bin_index] += self.valueof(item)
        return bins

    def sums(self, bins: BinsArray) -> Tuple[float]:
        return bins


class BinnerKeepingContents(BinnerKeepingSums):
    """
    A binner that creates bin-arrays that keep track of the entire contents of each bin.

    >>> values = {"a":3, "b":4, "c":5, "d":5, "e":5}
    >>> binner = BinnerKeepingContents(lambda x: values[x])
    >>> bins = binner.new_bins(3)
    >>> printbins(binner.add_item_to_bin(bins, item="a", bin_index=0))
    Bin #0: ['a'], sum=3.0
    Bin #1: [], sum=0.0
    Bin #2: [], sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="b", bin_index=1)
    >>> printbins(bins)
    Bin #0: ['a'], sum=3.0
    Bin #1: ['b'], sum=4.0
    Bin #2: [], sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="c", bin_index=1);
    >>> printbins(bins)
    Bin #0: ['a'], sum=3.0
    Bin #1: ['b', 'c'], sum=9.0
    Bin #2: [], sum=0.0
    """

    def __init__(self, valueof: Callable = lambda x: x):
        super().__init__(valueof)

    BinsArray = Tuple[np.ndarray, List[List]]  # Here, each bins-array is a tuple: sums,lists. sums is an array of sums; lists is a list of lists of items.

    def new_bins(self, numbins: int) -> BinsArray:
        sums = np.zeros(numbins)
        lists = [[] for _ in range(numbins)]
        return (sums, lists)

    def add_item_to_bin(self, bins: BinsArray, item: Any, bin_index: int) -> BinsArray:
        sums, lists = bins
        value = self.valueof(item)
        sums[bin_index] += value
        lists[bin_index].append(item)
        return bins

    def sums(self, bins: BinsArray) -> Tuple[float]:
        return bins[0]


if __name__ == "__main__":
    import doctest, sys

    (failures, tests) = doctest.testmod(report=True, optionflags=doctest.FAIL_FAST)
    print("{} failures, {} tests".format(failures, tests))
    if failures > 0:
        sys.exit(19 )