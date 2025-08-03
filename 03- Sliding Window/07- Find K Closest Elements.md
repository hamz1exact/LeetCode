# 7.  Find K Closest Elements

Difficulty: Medium

[Problem Link](https://neetcode.io/problems/minimum-size-subarray-sum?list=neetcode250)

$$
The Problem
$$

**You are given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.**

**An integer `a` is closer to `x` than an integer `b` if:**

**`|a - x| < |b - x|`, or`|a - x| == |b - x|` and `a < b`**

- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

$$
Example
$$

```markdown
Input: arr = [2,4,5,8], k = 2, x = 6

Output: [4,5]
```

$$
Solution
$$

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        return arr[left:right+1]
```

$$
Explaining
$$

```markdown
if the absolute value of the left PTR is greater than the Right PTR
it means that the left PTR is too big to be closest, so we increment it
otherwise we increment right.
we do need to check left first then right.
```

$$
Stuck-Point
$$

```markdown
* How to Find The Closest Value.
```