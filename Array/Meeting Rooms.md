# 252. Meeting Rooms

Link: https://neetcode.io/problems/meeting-schedule
Difficulty: Easy
Status: Mastred
Patterns: Indexing, Iteration
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 3, 2025 9:23 PM

$$
Solution
$$

```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
```

$$
Explaining
$$

```

```

$$
Stuck-Point
$$

```

```

[**252. Meeting Rooms**
Easy](https://leetcode.com/problems/meeting-rooms)