# 29. Merge Strings Alternately

Link: https://leetcode.com/problems/merge-strings-alternately/description/
Difficulty: Easy
Status: Mastred
Patterns: Indexing
Priority: Low
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)

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
Explaining
$$

```
The Idea is we keep appending Characters as long as the Pointer that point to the word is less than its length (length of the word)
```

$$
Stuck-Point
$$

```
Null
```