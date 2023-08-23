arr: list[int] = [0] * 5
nums:list[int] = [1,2,3,4,5,6,7]

def extend(nums: list[int], enlarge:int) -> list[int]:
    # 扩展数组长度
    res = [0] * (len(nums)+enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

def insert(nums: list[int], num: int, index: int):
    # insert a number before the index of array
    #nums = nums.append(0)这是错误的写法，append方法不会返回任何参数
    nums.append(0)
    for i in range(len(nums)-1,index,-1):
        nums[i] = nums[i-1]
    nums[index] = num
    return nums


print(insert(nums,0,0))

def remove(nums:list[int],index:int):
    for i in range(index,len(nums)-1):
        nums[i] = nums[i+1]
    return nums


def a():
    ab = 1
    ba = 3
    b(ab,ba)
    print(ab,ba)


def b(num1,num2):
    num1 += 1
    num2 += 2
    return

a()

e = input('asdf')
e.split()
print(e)