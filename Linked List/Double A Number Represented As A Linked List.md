# 2816. Double a Number Represented as a Linked List

Difficulty: Medium
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.set_int_max_str_digits(100000000)  # or any limit bigger than your input size
        total = ""
        dummy = ListNode(0)
        prev = dummy
        current = head
        while current:
            total += str(current.val)
            current = current.next
        total = str(int(total) * 2)
        for i in range(len(total)):
            newNode = ListNode(int(total[i]))
            prev.next = newNode
            prev = prev.next
        return dummy.next
        
```

$$
Optimal-Solution
$$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list so we can process from least significant digit
        head = self.reverse(head)

        carry = 0
        current = head
        prev = None

        while current:
            val = current.val * 2 + carry
            current.val = val % 10
            carry = val // 10
            prev = current
            current = current.next

        # If we still have a carry after last node, add a new node
        if carry:
            prev.next = ListNode(carry)

        # Reverse back to original order
        return self.reverse(head)

    def reverse(self, head):
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
```

$$
Explaining
$$

```
1) Reverse the list

Copy
Edit
1 → 8 → 9   =>   9 → 8 → 1
2) Walk from left to right (now least-significant first), doubling each node and carrying

Start: carry = 0

Node 9:

val = 9*2 + 0 = 18

write 18 % 10 = 8 to node

carry = 18 // 10 = 1

list now: 8 → 8 → 1, carry=1

Node 8:

val = 8*2 + 1 = 17

write 17 % 10 = 7

carry = 17 // 10 = 1

list now: 8 → 7 → 1, carry=1

Node 1:

val = 1*2 + 1 = 3

write 3 % 10 = 3

carry = 3 // 10 = 0

list now: 8 → 7 → 3, carry=0

End of list, carry = 0 so we don’t add a new node.

3) Reverse back to original order

8 → 7 → 3   =>   3 → 7 → 8
Result: [3, 7, 8] (i.e., 378), which is 2 × 189.

```

$$
Stuck-Point
$$

```

```