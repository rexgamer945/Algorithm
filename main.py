  

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([1,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,00,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,11,0,1,1,0,1,1,1096969766423155]))