# 725. Split Linked List in Parts

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Linked List
Time Complexity: O(n)
Space Complexity: O(n)
Created time: September 2, 2025 1:31 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        ans = []
        
        # Count length
        while current:
            n += 1
            current = current.next
        
        # Base size and remainder
        m = n % k
        f = n // k
        
        current = head
        for _ in range(k):
            part_head = current
            size = f + (1 if m > 0 else 0)
            m -= 1 if m > 0 else 0
            
            # Traverse size-1 nodes
            for _ in range(size - 1):
                if current:
                    current = current.next
            
            # Cut link
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            ans.append(part_head)  # append head (may be None)
        
        return ans

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