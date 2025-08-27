# 10- Design Circular Queue

$$
The Problem
$$

**Design and implement circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".**

**One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.**

**Implement the `MyCircularQueue` class:**

**`MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.`int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.`int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.`boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.`boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.`boolean isEmpty()` Checks whether the circular queue is empty or not.`boolean isFull()` Checks whether the circular queue is full or not.**

- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.
- `int Front()` Gets the front item from the queue. If the queue is empty, return `1`.
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `1`.
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.
- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.
- `boolean isEmpty()` Checks whether the circular queue is empty or not.
- `boolean isFull()` Checks whether the circular queue is full or not.

$$
Example
$$

```markdown
Input: ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output: [null, true, true, true, false, 3, true, true, true, 4]

```

$$
Solution
$$

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:
    def __init__(self, k):
        self.tail = ListNode(-1)
        self.head = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.k = k
        self.n = 0
    def enQueue(self, value):
        if self.n < self.k:
            self.n+=1
        else:
            return False
        node = ListNode(value)
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        return True
    def deQueue(self):
        if self.n == 0:
           return False
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.n -= 1
        return True
    def Front(self):
        if self.n == 0:
           return -1
        print()
        return self.head.next.val
    def Rear(self):
       if self.n ==0:
           return -1
       return self.tail.prev.val
    def isEmpty(self):
       if self.n ==0:
           return True
       return False
    def isFull(self):
       if self.n == self.k:
           return True
       return False
```

$$
Explaining
$$

```markdown
Null
```

$$
Stuck-Point
$$

```markdown
Null
```