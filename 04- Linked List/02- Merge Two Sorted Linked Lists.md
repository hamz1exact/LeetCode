# 02- Merge Two Sorted Linked Lists

Difficulty: Easy
Status: Mastred
Priority: High
Time Complexity: O(n)
Space Complexity: Null
Link: https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode250

$$
The Problem
$$

**You are given the heads of two sorted linked lists `list1` and `list2`.**

**Merge the two lists into one sorted linked list and return the head of the new sorted linked list.**

**The new list should be made up of nodes from `list1` and `list2`.**

$$
Example
$$

![](image/image.png)

```markdown
Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        Dummy = ListNode(0)
        Dummy.next = list1
        current = Dummy
        while list1 and list2:
            if list1.val == list2.val:
                current.next = list1            
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            elif list2.val > list1.val:
                current.next = list1
                list1 = list1.next
            current = current.next
        current.next = list1 or list2
        return Dummy.next
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