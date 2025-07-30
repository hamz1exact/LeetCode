# 9. Design HashSet

Difficulty: Easy
Status: Mastred
Priority: High
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/design-hashset?list=neetcode250

$$
Solution
$$

```python
class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data

```

$$
Explaining
$$

```
We Used Some Array Functions
```