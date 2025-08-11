# 06- Remove Nth Node From End of List

Difficulty: `Medium`

Priority: `High`

Time Complexity: `O(n)`

[Problem Link](https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode250)

$$
The Problem
$$

**You are given the beginning of a linked list `head`, and an integer `n`.**

**Remove the `nth` node from the end of the list and return the beginning of the list.**

$$
Example
$$

![](image/image4.png)

```markdown
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n == 0:
            return
        elif head and head.next == None and n == 1:
            head = None
            return head
        head = head
        dummy = ListNode(0, head)
        second = dummy
        first = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
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