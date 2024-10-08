from turtledemo.sorting_animate import partition


def swap(a, b, array):
    if a!=b:
        array[a], array[b] = array[b], array[a]


def hoare_partition(elements, start, end):

    # Hoare Partition
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:

        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] >= pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def lomuto_partition(elements, start, end):

    pivot_index = end
    pivot = elements[pivot_index]
    i = 0

    while i < end:

        while elements[start] < pivot:
            start += 1

        i = start

        while elements[i] > pivot and i < len(elements):
            i += 1

        swap(start, i, elements)

    return start


def quick_sort(elements, start, end, partition='hoare'):
    if start < end:
        if partition == 'hoare':
            pi = hoare_partition(elements, start, end)
        elif partition == 'lomuto':
            pi = lomuto_partition(elements, start, end)
        else:
            print("Name of partition not supported. Choices: hoare, lomuto")
            return
        quick_sort(elements, start, pi-1, partition) #left partition
        quick_sort(elements, pi+1, end, partition) #right partition

if __name__ == "__main__":
    #Using Hoare Partition
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0 , len(elements)-1, partition='hoare')
    print(elements)
    #Using Lomuto Partition
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1, partition='lomuto')
    print(elements)

