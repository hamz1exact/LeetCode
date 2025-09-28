# 1721. Swapping Nodes in a Linked List

Difficulty: Medium
Patterns: Fast & Slow Pointer
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(1)

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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return 
        dummy = ListNode(0, head)
        FirstkthNode = dummy
        fast, slow = dummy, head
        for _ in range(k):
            FirstkthNode = FirstkthNode.next
        for _ in range(k + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.val, FirstkthNode.val = FirstkthNode.val, slow.val
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