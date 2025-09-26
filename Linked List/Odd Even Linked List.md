# 328. Odd Even Linked List

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 11, 2025 3:32 AM

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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        backUp = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = backUp
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