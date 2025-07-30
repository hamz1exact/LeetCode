# 29. Merge Strings Alternately

Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Status: Mastred
Patterns: Indexing
Priority: Low
Topic: Array & String
Time Complexity: O(n)
Space Complexity: NULL

$$
Solution
$$

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '' :return True
        if len(s) > len(t): return False
        i = 0
        for k in range(len(t)):
            if t[k] == s[i]:
                if i == len(s) - 1:
                    return True
                i +=1
        return False
```

$$
Explaining
$$

```
We increment S word's Pointer only of a match found, if all matches we return True, False Otherwise
```

$$
Stuck-Point
$$

```
Null
```