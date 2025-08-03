# 4. Longest Repeating Character Replacement

Difficulty: Medium

Link: [Problem Link](https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150)

$$
The Problem
$$

**You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.**

**After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.**

$$
Example
$$

```markdown
Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

-------------------------------

Input: s = "AAABABB", k = 1

Output: 5
```

$$
Solution
$$

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size = 0
        window_size = 0
        l = 0
        count = {}
        for r in range(len(s)):
            window_size = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if window_size - max(count.values()) <= k:
                max_size = max(max_size, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return max_size
        
        
# Solution 2 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
	    max_size, l, window_size, max_char = 0, 0, 0, 0
	    count = {}
	    for r in range(len(s)):
	        window_size = r - l + 1
	        count[s[r]] = count.get(s[r], 0) + 1
	        max_char = max(max_char, count.get(s[r]))
	        if window_size - max_char <= k:
	            max_size = max(max_size, r - l + 1)
	        else:
	            count[s[l]] -= 1
	            l += 1
	    return max_size
```

$$
Explaining
$$

```markdown
* Once You Get The Equation, You Done
* The Equation was (window_size - maxCharFreqValue <= k)
	which means the current window - the most repeated chars

```

$$
Stuck-Point
$$

```markdown
* How to recalculate the Window.
```