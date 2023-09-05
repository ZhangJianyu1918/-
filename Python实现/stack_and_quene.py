from linked_list import ListNode
from typing import Optional
import collections

class LinkedListStack:
    # based on linkedlist realize stack

    def __init__(self) -> None:
        self.__peek: Optional[ListNode] = None
        self.__size: int = 0

    def size(self) -> int:
        # achieve the length stack
        return self.__size
    
    def is_empty(self) -> bool:
        # judge if the stack is empty
        return not self.__peek
    
    def push(self, value: int):
        node = ListNode(value)
        node.next = self.__peek
        self.__peek = node
        self.__size += 1

    def pop(self) ->int:
        num: int = self.peek()
        self.__peek = self.__peek.next
        self.__size -= 1
        return num

    def peek(self) -> int:
        if not self.__peek:
            return None
        return self.__peek.value
    
    def to_list(self) -> list[int]:
        # transfer stack to a printable list
        arr = []
        node = self.__peek
        while node:
            arr.append(node)
            node = node.next
        arr.reverse()
        return arr
        
# test code
n = LinkedListStack()
n.push(2)
n.push(3)
n.push(4)
print(n.peek())
n.pop()
print(n.peek())
n.push(3)
n.push(4)
print(type(n))
print(type(n.to_list()))


class linkedListQueue:
    # realize queue based on linked list

    def __init__(self) -> None:
        self.__front: Optional[ListNode] = None
        self.__rear: Optional[ListNode] = None
        self.__size: int = 0

    def size(self) ->int:
        return self.__size
    
    def is_empty(self) -> int:
        return not self.__front
    
    def push(self, num: int):
        node = ListNode(num)
        if self.__front == None:
            # if queue is empty, make front and rear each direction to this node
            self.__front = node
            self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node
        self.__size += 1

    def pop(self) -> int:
        num = self.peek()
        self.__front = self.__front.next
        self.__size -= 1
        return num
    
    def peek(self) -> int:
        if self.size() == 0:
            print('empty queue')
            return False
        return self.__front.value
    
    def to_list(self) -> list[int]:
        arr = []
        while self.__front:
            arr.append(self.__front)
            self.__front = self.__front.next
        return arr

# test code
n = linkedListQueue()
n.push(2)
n.push(3)
n.push(4)
print(n.peek())
n.pop()
print(n.peek())
n.push(3)
n.push(4)
print(type(n))
print(type(n.to_list()))

# use collections.deque to create a queue
# it create a doubly queue
queue = collections.deque()
queue.append(1) # append element at tail of queue
queue.append(2)
queue.appendleft(0) # append element at head of queuequeue.appendleft(12) # append element at head of queue
queue.appendleft(-1) # append element at head of queue
print(queue)
print(queue.pop())
print(queue.popleft())
print(queue)
print(len(queue))


class LinkedListDoublyQueue:
    # realize DoublyQueue based on Doubly List
    def __init__(self) -> None:
        self.__front: Optional[ListNode] = None
        self.__rear: Optional[ListNode] = None
        self.__size: int = 0

    def size(self):
        return self.__size
    
    def is_empty(self):
        return not self.__front
    
    def push(self, num: int, is_front: bool):
        node = ListNode(num)
        if self.is_empty():
            self.__front = node
            self.__rear = node
        elif is_front:
            self.__front.prev = node
            node.next = self.__front
            self.__front = node
        else:
            self.__rear.next = node
            node.prev = self.__rear
            self.__rear = node
        self.__size += 1

    def push_frist(self,num:int):
        self.push(num,True)

    def push_last(self,num:int):
        self.push(num,False)

    def pop(self,is_front):
        if self.is_empty():
            return None
        elif is_front:
            num = self.__front.value
            node: Optional[ListNode] = self.__front.next
            if node != None:
                node.prev = None
                self.__front.next = None
            self.__front = node
        else:
            num = self.__rear.value
            node: Optional[ListNode] = self.__rear.prev
            if node != None:
                node.next = None
                self.__rear.prev = None
            self.__rear = node
        self.__size -= 1
        return num
    
    def pop_frist(self):
        return self.pop(True)

    def pop_last(self):
        return self.pop(False)

    def peek_frist(self):
        return self.__front.value
    
    def peek_last(self):
        return self.__rear.value
    
    def to_array(self) -> list:
        arr = [0] * self.size()
        node = self.__front
        for index in range(self.size()):
            arr[index] = node.value
            node = node.next
        return arr
    
queue = LinkedListDoublyQueue()
queue.push_last(1) # append element at tail of queue
queue.push_last(3)
queue.push_frist(0) # append element at head of queuequeue.appendleft(12) # append element at head of queue
queue.push_frist(-1) # append element at head of queue
print(queue.to_array())
print(queue.pop_last())
print(queue.pop_frist())
print(queue)
print(queue.to_array())