# 61. Rotate List

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 10, 2025 2:37 AM

$$
Solution
$$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        # dummy = Node(0,head)
        # k = k % l 
        # dummy = node(0, self.head)
        length = 0
        current = head
        while current:
            length  += 1
            current = current.next 
        k = k % length
        for _ in range(k):
            current = head   
            while current and current.next:
                if current.next.next == None:
                    currtemp = current
                    nextTemp = current.next
                    current.next = None
                    nextTemp.next = head
                    head = nextTemp
                current = current.next
        return head
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