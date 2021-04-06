import random
import cProfile

def bubble_sort(list):
    """
        冒泡排序
        Args:
            list (list): 待排序列表
    """
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

lst = random.choices(range(1000), k=10000)
cProfile.run("bubble_sort(lst)")