import random
import time


def get_number_list(amount: int) -> list:
    result = []
    for _ in range(amount):
        result.append(random.randint(1, 100000))

    return result


def merge_sort(arr)-> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right)-> list:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst)-> list:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def get_copy_list(item: list)-> list:
    return item.copy()


random_numbers = get_number_list(20000)
print(len(random_numbers))

numbers = get_copy_list(random_numbers)
start_time = time.time()
insertion_sort(numbers)
print(f"Insert sort : {time.time() - start_time} sec")

numbers = get_copy_list(random_numbers)
start_time = time.time()
merge_sort(numbers)
print(f"Merge sort : {time.time() - start_time} sec")

numbers = get_copy_list(random_numbers)
start_time = time.time()
sorted(numbers)
print(f"Python function sorted : {(time.time() - start_time)} sec")