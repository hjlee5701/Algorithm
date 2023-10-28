class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = target+1
        total, left = 0, 0
        for idx in range(len(nums)):
            total += nums[idx]

            while total >= target:
                res = min(res, idx-left+1)
                total -= nums[left]
                left +=1
        
        return res if res != target+1 else 0