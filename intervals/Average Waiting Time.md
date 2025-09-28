# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Difficulty: Medium
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        summ = 0
        ans = 0
        for r in range(len(arr)):
            summ += arr[r]
            if r - l + 1 == k:
                if summ // k >= threshold:
                    ans += 1
                summ -= arr[l]
                l += 1
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