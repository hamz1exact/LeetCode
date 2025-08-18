# 01- Baseball Game

Difficulty: Easy

$$
The Problem
$$

**You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.**

**Given a list of strings `operations`, where `operations[i]` is the `ith` operation you must apply to the record and is one of the following:**

**An integer `x`: Record a new score of `x`.'+': Record a new score that is the sum of the previous two scores.'D': Record a new score that is the double of the previous score.'C': Invalidate the previous score, removing it from the record.**

- **An integer `x`: Record a new score of `x`.**
- **'+': Record a new score that is the sum of the previous two scores.**
- **'D': Record a new score that is the double of the previous score.**
- **'C': Invalidate the previous score, removing it from the record.**

**Return the sum of all the scores on the record after applying all the operations.**

**Note: The test cases are generated such that the answer and all intermediate calculations fit in a `32`-bit integer and that all operations are valid.**

$$
Example
$$

```markdown
Input: ops = ["1","2","+","C","5","D"]

Output: 18
```

$$
Solution
$$

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        prev = 0
        stack = []
        for op in operations:
            if op.isdigit() or  (op.startswith('-') and op[1:].isdigit()):
                stack.append(int(op))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                prev = 1 if prev == 0 else prev
                stack.append(2 * stack[-1])
            elif op == '+':
                first_score = stack[-1] if stack[-1] else 0
                second_score = stack[-2] if stack[-2] else 0
                stack.append(first_score + second_score) 
            prev = stack[-1] if stack else None
        return sum(stack)
```

$$
Explaining
$$

```markdown
Null
```

$$
Stuck-Point
$$

```markdown
Null
```