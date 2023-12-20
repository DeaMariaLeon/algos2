#Insertion Sort
import time

def sort(array: list[int]) -> list[int]:
    time.sleep(1.2)
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    #time.sleep(3)
    return array
