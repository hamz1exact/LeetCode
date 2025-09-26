# 394. Decode String

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 28, 2025 12:56 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def decodeString(self, s: str) -> str:
        nstack = []
        cstack = []
        bstack = []
        r = 0
        finalString = ""
        
        while r < len(s):
            num = ""
            string = ""

            # Handle letters
            if r < len(s) and s[r].isalpha(): 
                while r < len(s) and s[r].isalpha(): 
                    string += s[r] 
                    r += 1
                if not bstack:
                    finalString += string
                else:
                    # FIX: append letters to the last string in cstack, don't push a new element
                    cstack[-1] += string

            # Handle digits
            elif r < len(s) and s[r].isdigit():
                while r < len(s) and s[r].isdigit():
                    num += s[r]
                    r += 1
                nstack.append(int(num))

            # Opening bracket
            elif r < len(s) and s[r] == '[':
                bstack.append('[')
                cstack.append("")  # start a new string for this bracket
                r += 1

            # Closing bracket
            elif r < len(s) and s[r] == ']':
                bstack.pop()
                multiplayer = nstack.pop() if nstack else 1
                char = cstack.pop()
                string = multiplayer * char
                if bstack:
                    cstack[-1] += string
                else:
                    finalString += string
                r += 1

        return finalString
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