# 05- Min Stack

Difficulty: Medium

$$
The Problem
$$

**Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations.**

**`MinStack()` initializes the stack object.`void push(int val)` pushes the element `val` onto the stack.`void pop()` removes the element on the top of the stack.`int top()` gets the top element of the stack.`int getMin()` retrieves the minimum element in the stack.**

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

**Each function should run in O(1)*O*(1) time.**

$$
Example
$$

```markdown
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

```

$$
Solution
$$

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
        
    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)	
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)
        return
        
        
    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
        
    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None

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