# 2130. Maximum Twin Sum of a Linked List

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 25, 2025 7:50 PM
Solved by my own: True

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
    def reverse(self, head):
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev 
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = self.reverse(slow)
        first = head
        max_count = 0
        while second:
            max_count = max(max_count, first.val + second.val)
            first = first.next
            second = second.next
        return max_count
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