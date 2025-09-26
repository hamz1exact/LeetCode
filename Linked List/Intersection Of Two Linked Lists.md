# 160. Intersection of Two Linked Lists

Difficulty: Easy
Status: Mastred
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 15, 2025 12:12 AM
Solved by my own: True

$$
Solution
$$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 1️⃣ Count lengths
        n1 = 0
        current = headA
        while current:
            n1 += 1
            current = current.next
        
        n2 = 0    
        current = headB
        while current:
            n2 += 1
            current = current.next
        
        # 2️⃣ Align starts
        diff = n1 - n2
        currA = headA
        currB = headB
        for _ in range(abs(diff)):
            if diff < 0:
                currB = currB.next
            else:
                currA = currA.next
        
        # 3️⃣ Move together until intersection found
        while currA and currB:
            if currA is currB:  # or id(currA) == id(currB)
                return currA
            currA = currA.next
            currB = currB.next
        
        return None
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