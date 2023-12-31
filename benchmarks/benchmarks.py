# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from insertion_sort import sort
import random

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    
    def setup(self):
        LENGTH = 10
        #random.seed(10)
        self.array = [random.randint(0, 1000) for i in range(LENGTH)]

    def time_insertion_sort(self):
        sort(self.array)

    time_insertion_sort.date_scale = "True"
    time_insertion_sort.repeat = 3
    time_insertion_sort.number = 4
