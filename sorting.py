import random

test_array = [i for i in range(1, 26)]
random.shuffle(test_array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def shaker_sort(array):
    left = 1
    right = len(array) - 1
    while left <= right:
        for i in reversed(range(left, right + 1)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
        left += 1
        for i in range(left, right + 1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        right -= 1


def gnome_sort(array):
    current = 1
    while current < len(array):
        if current - 1 < 0:
            current += 1
        if array[current - 1] > array[current]:
            array[current - 1], array[current] = array[current], array[current - 1]
            current -= 1
        else:
            current += 1


def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


print(f'Массив до сортировки: {test_array}')
print(f'Массив после сортировки: {test_array}')
