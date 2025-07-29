class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentNum, count = 0, 0
        for num in nums:
            if count == 0:
                currentNum = num
            count += (1 if num == currentNum else -1 )
        return currentNum
