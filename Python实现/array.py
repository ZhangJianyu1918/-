def extend(nums: list[int], enlarge:int) -> list[int]:
    # 扩展数组长度
    res = [0] * (len(nums)+enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

