from typing import Optional

print('linked_list file')

class ListNode():
    def __init__(self, value:int):
        self.value:int = value
        self.next:Optional(ListNode) = None
        self.prev:Optional(ListNode) = None
    def __str__(self) -> str:
        return f'value:{self.value}'
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

def insert(node:ListNode, insert_node:ListNode):
    # insert inode after node in linked list
    # head insert
    insert_node.next = node.next
    node.next = insert_node

print(n1.next)
n5 = ListNode(23)
insert(n1,n5)
print(n1.next)

def remove(node:ListNode):
    # remove the frist Node after the node in linked list
    if node.next == None:
        return
    else:
        node.next = node.next.next

print(n1.next)
remove(n1)
print(n1.next)

def find(head:ListNode,target:int) -> int:
    # Traverse the linklist and find a node's value of target
    index = 0
    while head:
        if head.value == target:
            return index
        else:
            head = head.next
            index += 1
    return -1

class DoublyListNode():
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[DoublyListNode] = None
        self.prev: Optional[DoublyListNode] = None


a = [1,2,3]
b = [2,3,4]
# print the same memory address
# because python list store the 
print(id(a[1]),id(b[0]))

class mylist:
    # create a simple list
    def __init__(self) -> None:
        self.__capacity: int = 10 # list capacity
        self.__nums: list[int] = [0] * self.__capacity # array
        self.__size: int = 0 #list length
        self.__extend_ratio: int = 2 # the times of expansion array

    def size(self) ->int:
        # achieve the current length of list
        return self.__size
    
    def capacity(self) ->int:
        # get the capacity of the list
        return self.__size
    
    def get(self, index: int) ->int:
        # access element
        if index < 0 or index >= self.__size:
            raise IndexError('index  out of range')
        return self.__nums[index]
    
    def add(self,num:int):
        # add the element at the tail of list
        if self.__size == self.__capacity:
            self.extend_capacity()
        self.__nums[self.__size] = num
        self.__size += 1

    def insert(self,num: int, index: int):
        # insert a element in list
        if index < 0 or index >= self.__size:
            raise IndexError('index out of range')
        if self.__size == self.__capacity:
            self.extend_capacity()
        # let the element between index and the last go back one position
        for i in range(self.__size-1, index-1 ,-1):
            self.__nums[i+1] = self.__nums[i]
        self.__nums[index] = num
        self.__size += 1

    def remove(self, index: int) -> int:
        # remove a element in according to the index in list
        if index < 0 or index >= self.__size:
            raise IndexError('index out of range')
        num = self.__nums[index]
        for i in range(index, self.__size-1):
            self.__nums[i] = self.__nums[i+1]
        self.__size += 1
        return num
    
    def extend_capacity(self):
        # extend the capacity of list
        # create a new list, its capacity is __extend_radio times 
        # to old list
        # and copy the data to new list
        self.__nums = self.__nums + [0] * self.capacity()*(self.__extend_ratio - 1)
        self.__capacity = len(self.__nums)

    def to_array(self) -> list[int]:
        # return a valid length of list
        return self.__nums[:self.__size]

