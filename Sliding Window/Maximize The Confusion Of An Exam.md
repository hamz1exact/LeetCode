# 2024. Maximize the Confusion of an Exam

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)
Created time: September 6, 2025 12:57 AM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        counter = {}
        max_cnt = 0
        max_freq = 0
        for r in range(len(answerKey)):
            counter[answerKey[r]] = counter.get(answerKey[r], 0) + 1
            max_freq = max(max_freq, counter.get(answerKey[r]))
            if (r-l+1) - max_freq <= k:
                max_cnt = max(max_cnt, r-l+1)
            else:
                counter[answerKey[l]] -= 1
                if counter[answerKey[l]] == 0:
                    del counter[answerKey[l]]
                l += 1
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