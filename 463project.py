import random
import time
import sys

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    equal = [x for x in arr if x == pivot]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

def hybrid_sort(arr):
    if len(arr) <= 10:
        return quick_sort(arr)
    else:
        return merge_sort(arr)

def generate_an_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def find_TimeMemory(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    memory_usage = sys.getsizeof(arr)

    return end_time - start_time, memory_usage

if __name__ == "__main__":
    array_size = 1000  # Adjust the size of the array as needed
    unsorted_array = generate_an_array(array_size)

    # Measure time and memory for hybrid sort
    hybrid_time, hybrid_memory = find_TimeMemory(hybrid_sort, unsorted_array.copy())

    # Measure time and memory for merge sort
    merge_time, merge_memory = find_TimeMemory(merge_sort, unsorted_array.copy())

    # Measure time and memory for quick sort
    quick_time, quick_memory = find_TimeMemory(quick_sort, unsorted_array.copy())

    print(f"Hybrid Sort - Time: {hybrid_time:.6f} seconds, Memory: {hybrid_memory} bytes")
    print(f"Merge Sort - Time: {merge_time:.6f} seconds, Memory: {merge_memory} bytes")
    print(f"Quick Sort - Time: {quick_time:.6f} seconds, Memory: {quick_memory} bytes")
