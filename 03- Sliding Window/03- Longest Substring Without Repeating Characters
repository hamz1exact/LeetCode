# 3. Longest Substring Without Repeating Characters

Difficulty: `Medium`

Link: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150

$$
The Problem
$$

**Given a string `s`, find the *length of the longest substring* without duplicate characters.**

**A substring is a contiguous sequence of characters within a string.**

$$
Example
$$

```markdown
Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.
```

$$
Solution
$$

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set ()
        l = 0
        current_max = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            current_max = max(current_max, r - l + 1)
        return current_max
```

$$
Explaining
$$

```markdown
* we Keep Appending chars as long as we have no duplicates,
	if so we start shrink.
```

$$
Stuck-Point
$$

```markdown
Null
```