# 04- Reorder Linked List

Difficulty: Medium

Priority: High

Time Complexity: O(n)

Space Complexity: O(1)

[Problem Link](https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode250)

$$
The Problem
$$

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

*Reorder the list to be on the following form:*

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

$$
Example
$$
![](image/image5.png)

```markdown
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmpNext = second.next
            second.next = prev
            prev = second
            second = tmpNext
        second = prev
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
Space O(1)
Time O(n)
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        head = head
        dummy = ListNode(0)
        current_new = dummy
        current_orig = head
        size = 0
        while current_orig:
            size +=1
            current_new.next = ListNode(current_orig.val)
            current_new = current_new.next
            current_orig = current_orig.next
        dummy = dummy.next
        current = dummy
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        dummy = prev
        x = 0
        ee = ListNode(0)
        original = head
        reversed = dummy
        c = 0
        while c < size:
            if x % 2 == 0:
                ee.next = original
                x = 1
                original = original.next
                ee = ee.next
            elif x % 2 == 1:
                ee.next = reversed
                x = 0
                reversed = reversed.next
                ee = ee.next
            c += 1
        ee.next = None
        return head
        
Space O(n)
Time O(n)
```

$$
Explaining
$$

```markdown
* Step1: Find The Middle of the List
* Step2: Cut the Linked List into 2 Parts
* Step3: Reverse The Second Part
* Step4: Merge The First Part with The Reversed Second Part
```

$$
Stuck-Point
$$

```markdown
Null
```