# 15. Range Sum Query 2D Immutable

Difficulty: Medium
Status: Practicing
Priority: High
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/range-sum-query-2d-immutable?list=neetcode250

$$
Solution
$$

```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix: return 
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols+1) for _ in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.prefix[i][j] = matrix[i-1][j-1] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return result
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