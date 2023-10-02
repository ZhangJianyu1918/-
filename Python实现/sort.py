import random

nums = [random.randint(0, i) for i in range(80, 100)]

"""选择排序"""


def selection_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1):
        # outside loop: the unsorted range is [i, n-1]
        k = i
        for j in range(i + 1, n):
            # inside loop: find the mininum value in unsorted range
            if nums[j] < nums[k]:
                k = j  # record the index of mininum value
        # exchange the mininum element with first element of unsorted range
        nums[i], nums[k] = nums[k], nums[i]
    return nums


"""冒泡排序"""


def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        # outside loop: unsorted range is [0, i]
        for j in range(i):
            # inside loop: exchange the maximun element in unsorted range with the right side
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort_with_flag(nums: list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break


"""插入排序"""


def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        # outside loop: sorted range is [0, i-1]
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            # inside loop: insert base into the correct position in sorted range[0,i-1]
            nums[j + 1] = nums[j]  # move nums[i] one right position
            j -= 1
        nums[j + 1] = base  # place base to suitable position


"""快速排序"""


def partition(nums: list[int], left: int, right: int) -> int:
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # find frist element that is less than base element from right to left
        while i < j and nums[i] <= nums[left]:
            i += 1  # find frist element that is more than base element from left to right
        nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[i] = nums[i], nums[left]
    return i


def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
        # must only satisfy one condition and another one can not be true
        return left
    elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
        return mid
    return right


def partition_three(nums: list[int], left: int, right: int) -> int:
    """choose the midden value in three number"""
    med = median_three(nums, left, (left + right) // 2, right)
    nums[left], nums[med] = nums[med], nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # find frist element that is less than base element from right to left
        while i < j and nums[i] <= nums[left]:
            i += 1  # find frist element that is more than base element from left to right
        nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[i] = nums[i], nums[left]
    return i


def quick_sort(nums: list[int], left: int, right: int) -> list:
    if left >= right:
        return nums
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


def quick_sort_optimization(nums: list[int], left: int, right: int):
    while left < right:
        pivot = partition(nums, left, right)
        if pivot - left < right - pivot:
            # choose the short array to recursion in advance
            # it optimize the worst space complexity to O(logn)
            quick_sort_optimization(nums, left, pivot - 1)
        else:
            quick_sort_optimization(nums, pivot + 1, right)


"""归并排序"""


def merge(nums: list[int], left: int, mid: int, right: int):
    tmp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    nums[left:right + 1] = tmp


def merge_sort(nums: list[int], left: int, right: int):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)



"""test code"""
print(nums)
# print(bubble_sort(nums))
# print(selection_sort(nums))
quick_sort(nums,0,len(nums)-1)
#merge_sort(nums=nums, left=0, right=len(nums) - 1)
print(nums)
