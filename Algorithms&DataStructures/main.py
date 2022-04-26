# Press the green button in the gutter to run the script.
from pprint import pprint
from random import randint
import numpy


def generate_random_array(length=101):
    random_list = []
    for i in range(length):
        random_list.append(randint(10, 100))
    return random_list

def generate_random_2d_array(rows=10, columns=10):
    some_2d_array = []
    for i in range(rows):
        some_list = generate_random_array(length=columns)
        some_2d_array.append(some_list)
    pprint(some_2d_array)
    return some_2d_array

def preliminary_task_1(some_list):
    print(min(some_list))
    print(max(some_list))
    sorted_upwards = sorted(some_list)
    print(sorted_upwards)
    sorted_downwards = sorted(some_list, reverse=True)
    print(sorted_downwards)


def task_1_a(generated_list):
    LEFT = True
    RIGHT = False
    some_list = []
    sorted_generated_list = sorted(generated_list, reverse=True)
    direction = LEFT
    for element in sorted_generated_list:
        if direction is RIGHT:
            some_list.append(element)
            direction = LEFT
        else:
            some_list.insert(0, element)
            direction = RIGHT
    print(some_list)


def task_1_b(generated_list):
    generated_list_cpy = list(generated_list)
    some_list = []
    counter = 0
    while len(generated_list_cpy) > 0:
        if counter % 2 == 0:
            maxima = max(generated_list_cpy)
            generated_list_cpy.remove(maxima)
            some_list.append(maxima)
        else:
            minima = min(generated_list_cpy)
            generated_list_cpy.remove(minima)
            some_list.append(minima)
        counter += 1
    print(some_list)


def task_1_c(generated_list):
    odd = []
    even = []
    for index, element in enumerate(generated_list):
        if index % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    print(sorted(even, reverse=True) + sorted(odd))


def task_2_a(generated_2d):
    for lst in generated_2d:
        for element in lst:
            print(element, end=' ')
        print()

def task_2_b(generated_2d):
    cols = len(generated_2d)
    rows = len(generated_2d[0])
    for i in range(rows):
        for j in range(cols):
            print(generated_2d[j][i], end=' ')
        print()


def task_2_c(generated_2d):
    list_1d = generate_spiral_order(generated_2d)

    size = len(generated_2d[0])
    for i in range(size):
        for j in range(size):
            print(list_1d[i * size + j], end=" ")
        print()

def task_2_d(generated_2d):
    list_1d = generate_spiral_order_down(generated_2d)
    list_1d.reverse()
    size = len(generated_2d[0])
    for i in range(size):
        for j in range(size):
            print(list_1d[i * size + j], end=" ")
        print()


def generate_spiral_order(generated_2d):
    list_1d = []
    step = len(generated_2d[0])
    row_index = 0
    col_index = 0
    while step > 0:
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            col_index += 1
        col_index -= 1
        row_index += 1
        step -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            row_index += 1
        row_index -= 1
        col_index -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            col_index -= 1
        col_index += 1
        row_index -= 1
        step -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            row_index -= 1
        row_index += 1
        col_index += 1
    return list_1d

def generate_spiral_order_down(generated_2d):
    list_1d = []
    step = len(generated_2d[0])
    row_index = 0
    col_index = 0
    while step > 0:
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            row_index += 1
        row_index -= 1
        col_index += 1
        step -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            col_index += 1
        col_index -= 1
        row_index -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            row_index -= 1
        row_index += 1
        col_index -= 1
        step -= 1
        for i in range(step):
            list_1d.append(generated_2d[row_index][col_index])
            col_index -= 1
        col_index += 1
        row_index += 1
    return list_1d


def task_2_e(generated_2d):
    for index, row in enumerate(generated_2d):
        if index % 2 == 0:
            print(row)
        else:
            print(list(reversed(row)))

def task_2_f(generated_2d):

    list_1d = []
    col = 0
    is_reversed = False
    while col < len(generated_2d[0]):
        if is_reversed:
            iterated = reversed(generated_2d)
            is_reversed = False
        else:
            iterated = generated_2d
            is_reversed = True

        for index, lst in enumerate(iterated):
            if index % 2 == 0:
                for el in lst[col:col + 2]:
                    list_1d.append(el)
            else:
                for el in reversed(lst[col:col + 2]):
                    list_1d.append(el)
        col += 2

    size = len(generated_2d[0])
    for i in range(size):
        for j in range(size):
            print(list_1d[i * size + j], end=" ")
        print()


def generate_3d(size=5):
    return numpy.random.randint(1, 25, (size, size, size))



def task_3():
    sample_3d = generate_3d()
    flattened_3d = sample_3d.flatten()
    print(min(flattened_3d))
    print(max(flattened_3d))
    print('First axis:')
    print(numpy.sort(sample_3d, 0))
    print('Second axis:')
    print(numpy.sort(sample_3d, 1))
    print('Third axis:')
    print(numpy.sort(sample_3d, 2))


def task_4():
    set_1 = {1, 2, 3}
    set_2 = {2, 3, 4}
    print("Union: ")
    print(set_1.union(set_2))
    print("Intersection: ")
    print(set_1.intersection(set_2))
    print("Complementary: ")
    print(set_1.union(set_2) - set_1)
    print("Difference: ")
    print(set_1 - set_2)
    print("Symmetric difference: ")
    print(set_1.union(set_2) - set_1.intersection(set_2))


if __name__ == '__main__':
    generated_list = generate_random_array()
    print("Generated list:")
    print(generated_list)

    print("Min, max, sorted, sorted downwards:")
    preliminary_task_1(generated_list)


    print("Max-middle:")
    task_1_a(generated_list)
    print("Max-min alternation:")
    task_1_b(generated_list)
    print("Even down, odd up:")
    task_1_c(generated_list)

    generated_2d = generate_random_2d_array(rows=6, columns=6)

    print('Row-first order 2d:')
    task_2_a(generated_2d)
    print('Column-first order 2d:')
    task_2_b(generated_2d)
    print('Spiral:')
    task_2_c(generated_2d)
    print('Reverse spiral:')
    task_2_d(generated_2d)
    print('Array left-right:')
    task_2_e(generated_2d)
    print('Array snake:')
    task_2_f(generated_2d)

    task_3()
    task_4()
    
    

