

def insertion_sort(numbers):

    for i in range(1, len(numbers)):
        j = i - 1
        anchor = numbers[i]
        while anchor < numbers[j] and j >= 0:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            j -= 1


if __name__ == '__main__':
    list_numbers = [167, 21, 11, 29, 17, 4, 25, 11, 32, 9, 154]
    insertion_sort(list_numbers)
    print(list_numbers)
