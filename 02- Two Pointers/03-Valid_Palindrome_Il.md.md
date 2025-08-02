# 3. Valid Palindrom II

Difficulty: Easy
Status: Not Started
Priority: Medium
Link: https://neetcode.io/problems/reverse-string?list=neetcode250

$$
Solution
$$

```python
    if len(s) < 2 : return True
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            skipL = s[l+1:r+1]
            skipR = s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]
        l += 1
        r -= 1
    return True
```

$$
Explaining
$$

```
We skip one char from left, and one char from right, and we check which one can return True
if both returns False, means there is no valid palindrome
```

$$
Stuck-Point
$$

```
how to skip that char from the given str
```