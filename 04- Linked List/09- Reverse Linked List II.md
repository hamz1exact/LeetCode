# 09- Reverse Linked List II

Difficulty: `Medium`

[Problem Link](https://neetcode.io/problems/reverse-linked-list-ii?list=neetcode250)

$$
The Problem
$$

**You are given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed), and return the reversed list.**

$$
Example
$$

![](image/image3.png)

```markdown
Input: head = [1,2,3,4,5], left = 1, right = 3

Output: [3,2,1,4,5]
```

$$
Solution-1
$$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0, head)
        priorLeft = dummy
        current = head
        for _ in range(left - 1):
            priorLeft, current = current, current.next
        prev = 0
        for _ in range(right - left + 1):
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        priorLeft.next.next = current
        priorLeft.next = prev
        return dummy.next 
        
```

$$
Solution-2
$$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        sublist_head = prev.next
        sublist_end = sublist_head
        for _ in range(right - left):
            sublist_end = sublist_end.next
        remining_nodes = sublist_end.next
        sublist_end.next = None
        reversed_subList = self.reverseList(sublist_head)
        prev.next = reversed_subList
        sublist_head.next = remining_nodes
        return dummy.next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None
        current = head
        while current:
            nt = current.next
            current.next = prev
            prev = current
            current = nt
        return prev
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