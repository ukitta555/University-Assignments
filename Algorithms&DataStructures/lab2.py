import numpy as np
import bintrees
import heapq
from lab2_lib_files.binomial_heap import heap


def binom_heap(random_list):
    heap_1 = heap([(el, str(el)) for el in random_list])
    heap_1.insert(2000)
    heap_2 = heap([(el, str(el)) for el in random_list])
    heap_2.extract_min()
    for x in heap_1:
        print(x, end=" ")
    print()
    for x in heap_2:
        print(x, end=" ")
    print()


def bin_tree(random_list):
    import bintrees
    tree = bintrees.BinaryTree()
    for x in random_list:
        tree.insert(x, str(x))

    def func(key, val):
        print(val, end=" ")

    tree.foreach(func=func, order=0)
    print()
    tree.foreach(func=func, order=1)
    print()
    tree.foreach(func=func, order=-1)
    print()

def red_black_tree(random_list):
    tree = bintrees.RBTree()
    for x in random_list:
        tree.insert(x, str(x))

    def func(key, val):
        print(val, end=" ")

    tree.foreach(func=func, order=0)
    print()
    tree.remove(random_list[0])
    tree.foreach(func=func, order=0)
    print()

def bin_heap(random_list):
    heap = list(random_list)
    heapq.heapify(heap)
    heapq.heappush(heap, 100500)
    print(heap)
    heapq.heappop(heap)
    print(heap)
    heapq.heappop(heap)
    print(heap)


def k_stat(random_list,k=5):
    return np.sort(random_list)[:k]


if __name__ == '__main__':
    random_list = np.random.randint(0, 101, size=15)
    print("BinTree")
    bin_tree(random_list)
    print("RBTree")
    red_black_tree(random_list)
    print("BinHeap")
    bin_heap(random_list)
    print("BinomHeap")
    binom_heap(random_list)
    print("K-Stat")
    print(k_stat(random_list))
