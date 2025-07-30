# 5. Longest Common Prefix

Difficulty: Easy
Status: Mastred
Priority: Medium
Category: Hashing, String
Time Complexity: O(n)
Space Complexity: O(1)
Link: https://neetcode.io/problems/concatenation-of-array?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
            output+=strs[0][i]
        return output
```

$$
Idea
$$

Input:
`strs = ["flower","flow","flight"]`

output: “fl”

We start with the first word in the strs list which is strs[0] (”flower”)

and we iterate over each word in the strs list (for s in strs)

the first expression said :if i was equal to the current word in the strs list we stop and return the results, this will prevent us from getting an index Error because its not guaranteed that all words have the same lenght.

the second Expression said: if s[i] means the current CHAR in the current word was not equal to the current CHAR in the first word (strs[0][i]) we immediatly return the output, otherwise everything is valid and we store the current CHAR because its common among all words.