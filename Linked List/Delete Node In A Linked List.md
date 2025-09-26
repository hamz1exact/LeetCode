# 3217. Delete Nodes From Linked List Present in Array

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 10, 2025 2:38 AM

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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not nums:
            return head
        dummy = ListNode(0, head)
        nums = set(nums)
        current = head
        clean = dummy
        while current:
            if current.val not in nums:
                clean.next = current
                clean = clean.next
            current = current.next
        clean.next = None
        return dummy.next
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