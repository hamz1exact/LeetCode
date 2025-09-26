# 2206. Divide Array Into Equal Pairs

Difficulty: Easy
Status: Mastred
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 10, 2025 2:30 AM

$$
Solution
$$

```python
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums) // 2
        nums.sort()
        if len(nums) < 2:
            return False
        i = 0
        j = 1
        c = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                c += 1
            else:
                return False
            i += 2
            j += 2
        if c == n :
            return True
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