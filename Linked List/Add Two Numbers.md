# 445. Add Two Numbers II

Difficulty: Medium
Status: Need to be reviewed
Priority: High
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 13, 2025 1:25 AM

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Str = ""
        l2Str = ""
        totalStr = ""
        answer = ListNode(0)
        ans = answer
        while l1 or l2:
            l1Str += (str(l1.val) if l1 else "")
            l2Str +=(str(l2.val) if l2 else "")
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        totalStr = str(int(l1Str) + int(l2Str))
        for i in range(len(totalStr)):
            newNode = ListNode(int(totalStr[i]))
            ans.next = newNode
            ans = ans.next
        return answer.next
        
```

$$
Optimal - Solution
$$

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while stack1 or stack2 or carry:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            total = x + y + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head
            head = node
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