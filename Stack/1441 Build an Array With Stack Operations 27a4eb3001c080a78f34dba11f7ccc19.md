# 1441. Build an Array With Stack Operations

Difficulty: Medium
Status: Mastred
Priority: Low
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: September 26, 2025 11:28 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        stack = []
        target = set(target)
        cnt = 0
        for i in range(1, n+1):
            stack.append("Push")
            cnt+=1
            if i not in target:
                stack.append("Pop")
                cnt-=1
            if cnt == len(target):
                break
        return stack

```

$$
Optimazed-Solution
$$

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = ""
        target = set(target)
        cnt = 0
        for i in range(1, n+1):
            if len(out) == 0:
                out+="Push"
            else:
                out+="-Push"
            cnt+=1
            if i not in target:
                out+="-Pop"
                cnt-=1
            if cnt == len(target):
                break
        return out.split("-")
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