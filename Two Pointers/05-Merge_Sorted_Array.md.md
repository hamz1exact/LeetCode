# 5. Merge Sorted Array

Difficulty: Medium
Status: Not Started
Link: https://neetcode.io/problems/merge-sorted-array?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = m-1, n-1
        for i in range(len(nums1)-1, -1, -1):
            if x < 0:
                nums1[i] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
        
```

$$
Explaining
$$

```markdown
# Null
```

$$
Stuck-Point
$$

```markdown
# How to Prevent duplicated Values
```