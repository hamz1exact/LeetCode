# 594. Longest Harmonious Subsequence

Difficulty: Easy
Priority: Medium
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        freq = {}
        max_cnt = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if num - 1 in freq:
                max_cnt = max(max_cnt, freq[num] + freq[num-1])
            if num + 1 in freq:
                max_cnt = max(max_cnt, freq[num] + freq[num+1])

        return max_cnt

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