# 2108. Find First Palindromic String in the Array

Difficulty: Easy
Priority: Low
Topic: Array, Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

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