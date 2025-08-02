# 4. Merge Strings Alternately

Difficulty: Easy
Status: Practicing
Priority: Medium
Link: https://neetcode.io/problems/merge-strings-alternately?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and word2:
            return word2
        elif not word2 and word1:
            return word1
        elif not word2 and not word1:
            return ''

        rs = []
        l = 0
        r = 0
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                rs.append(word1[l])
                l+=1
            if r < len(word2):
                rs.append(word2[r])
                r+=1
        return ''.join(rs)
```

$$

$$