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

def selection_sort(list):
    """
        选择排序
        Args:
            list (list): 待排序列表
    """
    n = len(list)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if list[j] < list[minIndex]:
                minIndex = j
        if i != minIndex:
            list[i], list[minIndex] = list[minIndex], list[i]

def insertion_sort(list):
    """
        插入排序
        Args:
            list (list): 待排序列表
    """
    n = len(list)
    for i in range(1, n):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp

def shell_sort(list):
    """
        希尔排序
        Args:
            list (list): 待排序列表
    """
    gap = len(list)
    n = len(list)
    while gap > 1:
        gap //= 2
        for i in range(gap):
            for j in range(i+gap, n, gap):
                temp = list[j]
                k = j - gap
                while k >= 0 and list[k] > temp:
                    list[k+gap] = list[k]
                    k -= gap
                list[k+gap] = temp

def merge(list, start, mid, end, temp):
    """
        合并
        Args:
            list (list): 待排序列表
            start (int): 开始下标
            mid (int): 中间下标
            end (int): 结束下标
            temp (list): 临时列表
    """
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if list[i] <= list[j]:
            temp[k] = list[i]
            k += 1
            i += 1
        else:
            temp[k] = list[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = list[i]
        k += 1
        i += 1
    while j <= end:
        temp[k] = list[j]
        k += 1
        j += 1

    for i in range(k):
        list[start+i] = temp[i]

def merge_sort(list, start, end, temp):
    """
        归并排序
        Args:
            list (list): 待排序列表
            start (int): 开始下标
            end (int): 结束下标
            temp (list): 临时列表
    """
    if start < end:
        mid = (start + end) // 2
        merge_sort(list, start, mid, temp)
        merge_sort(list, mid+1, end, temp)
        merge(list, start, mid, end, temp)

def quick_sort(list, start, end):
    """
        快速排序
        Args:
            list (list): 待排序列表
            start (int): 开始下标
            end (int): 结束下标
    """
    if start < end:
        i = start
        j = end
        pivot = list[start]

        while i < j:
            while i < j and list[j] > pivot:
                j -= 1
            if i < j:
                list[i] = list[j]
                i += 1
            while i < j and list[i] < pivot:
                i += 1
            if i < j:
                list[j] = list[i]
                j -= 1
        
        list[i] = pivot
        quick_sort(list, start, i-1)
        quick_sort(list, i+1, end)