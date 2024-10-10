import pytest

def selection_sort(numbers):

    for i in range(len(numbers)-1):

        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        if i != min_index:
            numbers[i], numbers[min_index] = numbers[min_index] , numbers[i]

if __name__ == '__main__':

    number_list = [3, 38, 29, 17, 21, 25, 11, 32, 9]
    selection_sort(number_list)
    print(number_list)

# Parametrize test cases based on the given input lists
@pytest.mark.parametrize("numbers, expected", [
    ([89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], sorted([89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1])),
    ([], []),
    ([1, 5, 8, 9], [1, 5, 8, 9]),
    ([234, 3, 1, 56, 34, 12, 9, 12, 1300], sorted([234, 3, 1, 56, 34, 12, 9, 12, 1300])),
    ([78, 12, 15, 8, 61, 53, 23, 27], sorted([78, 12, 15, 8, 61, 53, 23, 27])),
    ([5], [5]),
])
def test_selection_sort(numbers, expected):
    selection_sort(numbers)
    assert numbers == expected
