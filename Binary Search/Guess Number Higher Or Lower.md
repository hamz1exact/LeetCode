# 374. Guess Number Higher or Lower

Difficulty: Easy
Priority: Low
Topic: Binary Search
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```rust
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
                let mut left: i32 = 1;
        let mut right: i32 = n;

        while left <= right {
            // use i64 to avoid overflow, then cast back
            let mid: i32 = left + (right - left) / 2;

            let res = guess(mid);
            if res == 0 {
                return mid;
            } else if res < 0 {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        -1
    }
    }

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