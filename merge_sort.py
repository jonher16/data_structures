import pytest

def merge_in_order(numbers1, numbers2):
    merged = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(numbers1) and pointer2 < len(numbers2):

        if numbers1[pointer1] <= numbers2[pointer2]:
            merged.append(numbers1[pointer1])
            if pointer1 < len(numbers1):
                pointer1 += 1
                continue

        if numbers2[pointer2] <= numbers1[pointer1]:
            merged.append(numbers2[pointer2])
            if pointer2 < len(numbers2):
                pointer2 += 1

    if pointer1 < len(numbers1):
        merged += numbers1[pointer1:]
    if pointer2 < len(numbers2):
        merged += numbers2[pointer2:]

    return merged

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    n = len(numbers)
    midpoint = n // 2
    left = numbers[:midpoint]
    right = numbers[midpoint:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_in_order(left, right)

if __name__ == "__main__":
    numbers_list_1 = [17, 21, 29, 38]
    numbers_list_2 = [4, 9, 25, 32]

    numbers_list = [56, 17, 21, 29, 38, 144, 4, 9, 25, 32]

    #print(merge_in_order(numbers_list_1, numbers_list_2))
    print(merge_sort(numbers_list))


# Test cases for merge_in_order
@pytest.mark.parametrize("numbers1, numbers2, expected", [
    ([], [], []),  # Both empty
    ([3], [], [3]),  # One list empty, other has one element
    ([], [5], [5]),  # One list empty, other has one element
    ([3], [5], [3, 5]),  # Both have single element
    ([5], [3], [3, 5]),  # Both have single element, reverse order
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),  # Interleaving elements
    ([10, 15, 20], [5, 17, 25], [5, 10, 15, 17, 20, 25]),  # Merged sorted order
])
def test_merge_in_order(numbers1, numbers2, expected):
    assert merge_in_order(numbers1, numbers2) == expected

# Test cases for merge_sort
@pytest.mark.parametrize("numbers, expected", [
    ([], []),  # Empty list
    ([3], [3]),  # Single element
    ([10, 3, 15, 7, 8, 23, 98, 29], [3, 7, 8, 10, 15, 23, 29, 98]),  # Image test case 1
    ([3], [3]),  # Single element
    ([9, 8, 7, 2], [2, 7, 8, 9]),  # Image test case 2
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted list
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse order list
])
def test_merge_sort(numbers, expected):
    assert merge_sort(numbers) == expected