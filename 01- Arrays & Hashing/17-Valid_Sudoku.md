# 17. Valid Sudoku

Difficulty: Medium
Status: Not Started
Priority: Medium
Category: Array, Hashing
Link: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = "."
        # Validate Rows
        for r in range(9):
            s = set()
            for c in range(9):
                token = board[r][c]
                if token in s:
                    return False
                elif token != empty:
                    s.add(token)
        # Validate Columns
        for r in range(9):
            s = set()
            for c in range(9):
                token = board[c][r]
                if token in s:
                    return False
                elif token != empty:
                    s.add(token)
        # Validate (3 x 3) Boxes
        intervals = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]

        for start, end in intervals:
            s = set()
            for i in range(start, start+3):
                for j in range(end, end+3):
                    token = board[i][j]
                    if token in s:
                        return False
                    elif token != empty:
                        s.add(token)
        return True
```

$$
Explaining
$$

```
Step1: We Validate all rows
Step2: We Validate All columns
Step3: We Validate All (3 x 3) Boxes 
```

$$
Stuck-Point
$$

```
How to Validate 3 x 3 Boxes, The Key behind this is making start and end of the interval of each box
```