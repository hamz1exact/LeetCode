# 12- Decode String

Difficulty: Medium

$$
The Problem
$$

**You are given an encoded string `s`, return its decoded string.**

**The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.**

**You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like `3a`, `2[4]`, `a[a]` or `a[2]`.**

**The test cases are generated so that the length of the output will never exceed `100,000`.**

$$
Example
$$

```markdown
Example 1:

Input: s = "2[a3[b]]c"

Output: "abbbabbbc"
Example 2:

Input: s = "axb3[z]4[c]"

Output: "axbzzzcccc"
Example 3:

Input: s = "ab2[c]3[d]1[x]"

Output: "abccdddx"
```

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
            if r < len(s) and s[r].isdigit():
                while r < len(s) and s[r].isdigit():
                    num += s[r]
                    r += 1
                nstack.append(int(num))

            # Opening bracket
            if r < len(s) and s[r] == '[':
                bstack.append('[')
                cstack.append("")  # start a new string for this bracket

            # Closing bracket
            if r < len(s) and s[r] == ']':
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

```markdown
Null
```

$$
Stuck-Point
$$

```markdown
Null
```