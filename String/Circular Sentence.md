# 622. Design Circular Queue

Difficulty: Medium
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)

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

```

```

$$
Stuck-Point
$$

```

```