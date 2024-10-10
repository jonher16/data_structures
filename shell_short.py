import pytest

def shell_sort(numbers):
    n = len(numbers)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            anchor = numbers[i]
            j = i
            while anchor <= numbers[j-gap] and j >= gap:
                numbers[j], numbers[j-gap] = numbers[j-gap], numbers[j]
                j -= gap

        gap //= 2

if __name__ == '__main__':
    number_list = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(number_list)
    print(number_list)

# Test cases using pytest
@pytest.mark.parametrize("numbers, expected", [
    ([89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], sorted([89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1])),
    ([], []),
    ([1, 5, 8, 9], [1, 5, 8, 9]),
    ([234, 3, 1, 56, 34, 12, 9, 12, 1300], sorted([234, 3, 1, 56, 34, 12, 9, 12, 1300])),
    ([5], [5]),
])
def test_shell_sort(numbers, expected):
    shell_sort(numbers)
    assert numbers == expected
