from src.algos2.insertion_sort import sort
import pytest
from statistics import median
import random

def test_1(benchmark):

    LENGTH = 1000
    random.seed(10)
    array = [random.randint(0, 1000) for i in range(LENGTH)]

    @benchmark
    def test_insertion_sort():
        sort(array)
    
    @benchmark
    def test_insertion2():
        median(array)

@pytest.mark.benchmark
def test_median_performance():
    return median([1, 2, 3, 4, 5])