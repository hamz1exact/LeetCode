# 01- Reverse Linked List

Difficulty: Easy

Status: Practicing

Priority: High

Time Complexity: O(n)

Space Complexity: Null

[Problem Link](https://neetcode.io/problems/reverse-a-linked-list?list=neetcode250)


$$
The Problem
$$

**Given the beginning of a singly linked list** `head`**, reverse the list, and return the new beginning of the list.**

$$
Example
$$

```markdown
Input: head = [1,2,3,4]

Output: [4,3,2,1]
```

$$
Solution
$$

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head:
            return
        current = head
        while current:
            next_temp_node = current.next
            current.next = prev
            prev = current
            current = next_temp_node
        return prev
```

$$
Explaining
$$

```markdown
* We Store The Next Node in next_temp_node
* Then We Set Current.next to point to prev which would be None in first iteration
* Set Prev to be whatever the current node is
* Move Forward to the Next node
******
- Later in the second iteration, prev is 1 so 2 will point to 1
- third iteration prev is 2 so 3 will point to 3
*** The Main idea is we set each new node to be the head.
we return prev because its the last value
```

$$
Stuck-Point
$$

```markdown
Null
```