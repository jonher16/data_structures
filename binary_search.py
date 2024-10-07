import time

def runtime_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Runtime of {func.__name__}: {runtime:.6f} seconds")
        return result
    return wrapper

@runtime_decorator
def linear_search(number_list, target):
    if not number_list: return -1
    for index, element in enumerate(number_list):
        if element == target: return index
    return -1

@runtime_decorator
def binary_search(number_list, target):
    if not number_list: return -1
    left_index = 0
    right_index = len(number_list)-1

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2
        number = number_list[mid_index]

        if number == target:
            return mid_index

        if number < target:
            left_index = mid_index + 1

        if number > target:
            right_index = mid_index - 1


    return -1

@runtime_decorator
def recursive_binary_search(number_list, target, left_index=0, right_index=None):
    if not number_list: return -1
    if right_index is None:
        right_index = len(number_list) - 1

    mid_index = (left_index+right_index) // 2

    if mid_index >= len(number_list) or mid_index < 0:
        return -1

    number = number_list[mid_index]

    if target == number:
        return mid_index

    if target < number:
        right_index = mid_index - 1
        return recursive_binary_search(number_list,target,left_index,right_index)

    if target > number:
        left_index = mid_index + 1
        return recursive_binary_search(number_list,target,left_index,right_index)



if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67, 78, 98, 105]
    number_to_find = 105
    index_linear = linear_search(numbers_list,number_to_find)
    index_binary = binary_search(numbers_list, number_to_find)
    index_recursive_binary = recursive_binary_search(numbers_list, number_to_find)
    print("Index (Linear): ", index_linear)
    print("Index (Binary): ", index_binary)
    print("Index (Recursive Binary): ", index_recursive_binary)

    print("Worst case scenario: 100000 in 100001 elements")

    numbers_list = [i for i in range(10000001)]
    number_to_find = 10000000
    index_linear = linear_search(numbers_list, number_to_find)
    index_binary = binary_search(numbers_list, number_to_find)
    print("Index (Linear): ", index_linear)
    print("Index (Binary): ", index_binary)