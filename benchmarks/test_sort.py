from algos_for_benchmarks.src.insertion_sort import sort
import random

def test_1(benchmark):

    LENGTH = 1000
    random.seed(10)
    array = [random.randint(0, 1000) for i in range(LENGTH)]

    @benchmark
    def time_insertion_sort():
        sort(array)
