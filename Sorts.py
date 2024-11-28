# Bubble sort
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


print('Bubble sort:', bubble_sort([4, 2, 6, 5, 1, 3]))


# Selection sort
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print('Selection sort:', selection_sort([4, 2, 6, 5, 1, 3]))


# Insertion sort
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j >= 0:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print('Insertion sort:', insertion_sort([4, 2, 6, 5, 1, 3]))


# Merge sort
def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


original_list = [3, 1, 4, 2]

sorted_list = merge_sort(original_list)

print('\n\nOriginal List:', original_list)

print('Merge Sorted List:', sorted_list)


# Quick sort
def quick_sort(my_list):
    if len(my_list) < 2:
        return my_list

    pivot = my_list[0]
    less = [i for i in my_list[1:] if i <= pivot]
    greater = [i for i in my_list[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

