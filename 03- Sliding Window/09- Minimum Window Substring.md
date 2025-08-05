# 09- Minimum Window Substring

Difficulty: Hard

[Problem Link](https://neetcode.io/problems/minimum-window-with-characters?list=neetcode250)

$$
The Problem
$$
Given two strings `s` and `t`, return the shortest **substring** of `s` such that every character in `t`, including duplicates, is present in the substring. If such a substring does not exist, return an empty string `""`.
You may assume that the correct output is always unique.
$$
Example
$$
```markdown
Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.
```
$$
Solution
$$
```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink window from the left
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

```
$$
Explaining
$$
```markdown
	1.	Count frequencies of characters in t
	2.	Initialize sliding window variables:
		•	left, right pointers
		•	have, need
		•	window dict
		•	res, resLen to track the smallest window
	3.	Start expanding window with right pointer over s
	4.	Update window count and check if a required character is fully matched
	5.	When have == need:
		•	Try to shrink the window from the left
		•	Update the result if the current window is smaller
		•	Update counts and have when moving left
	6.	Repeat until right reaches the end of s
	7.	Return the smallest valid window if found, else return empty string

```
$$
Stuck-Point
$$
```markdown

```