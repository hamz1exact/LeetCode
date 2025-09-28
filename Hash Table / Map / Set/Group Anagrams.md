# 25. Reverse Nodes in k-Group

Difficulty: Hard
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(n)

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        cnt = 0
        current = head
        while current:
            cnt += 1
            current = current.next
        dummy = ListNode(0)
        dummy.next = head
        dmtemp = dummy
        current = dummy.next
        while cnt >= k:
            prev = None
            for _ in range(k):
                nxt_temp = current.next
                current.next = prev
                prev = current
                current = nxt_temp
            last_node = dmtemp.next
            dmtemp.next.next = current
            dmtemp.next = prev
            dmtemp = last_node
            cnt -= k
        dmtemp.next = current
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