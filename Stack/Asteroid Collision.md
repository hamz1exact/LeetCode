# 735. Asteroid Collision

Difficulty: Medium
Priority: High
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            # Process potential collisions
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:   # Right asteroid smaller → explodes
                    stack.pop()
                    continue
                elif stack[-1] == -ast:  # Equal size → both explode
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
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
* How Do We Start Popping From Left
```