def bubble_sort(elements,key=None):

    n = len(elements)
    if not key:
        for i in range(n-1):
            swapped = False
            for j in range(n-1-i):
                if elements[j] > elements[j+1]:
                    temp = elements[j]
                    elements[j] = elements[j+1]
                    elements[j+1] = temp
                    swapped = True
            if not swapped:
                break
        return elements
    else:
        for i in range(n-1):
            swapped = False
            for j in range(n-1-i):
                if elements[j][key] > elements[j+1][key]:
                    temp = elements[j][key]
                    elements[j][key] = elements[j+1][key]
                    elements[j+1][key] = temp
                    swapped = True
            if not swapped:
                break
        return elements

if __name__ == "__main__":
    numbers = [5,2,98,54,578,33,6]
    print(bubble_sort(numbers))

    items = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    print(bubble_sort(items, key='name'))
