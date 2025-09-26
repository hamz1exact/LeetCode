# 2108. Find First Palindromic String in the Array

Difficulty: Easy
Status: Mastred
Priority: Low
Topic: Array, Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 23, 2025 2:12 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:

            if list(word) == list(word[::-1]):
                return word
        return ""
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