# 29. Merge Strings Alternately
Link: https://leetcode.com/problems/merge-intervals/description/
Difficulty: Medium
Status: Mastred
Patterns: Indexing
Priority: High
Topic: Array 
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda interval: interval[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged

```

$$
Explaining
$$

```
step1: we sort the intervals based on the start becuase each interval has [start, end]
step2: we iterate over each interval, if there is nothing in the merged array we immediately append whatever the interval was, but if its not empty we check if the end of the last interval in merged actually smaller than the start of the current interval, we append the array because there is no overlap (end < start for example [1,3][4,6] No overlap between 3 and 4 because 3 < 4)
if these conditions doesn't met, we keep the start of the merged array and we edit the end to be the bigger one.
```

$$
Stuck-Point
$$

```
Null
```