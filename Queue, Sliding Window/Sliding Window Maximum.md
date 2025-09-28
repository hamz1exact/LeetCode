# 239. Sliding Window Maximum

Difficulty: Hard
Priority: High
Topic: Queue, Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        ans = []
        r = l = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            if r - l + 1 >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
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