class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()

        for i in range(len(nums)):
            
            left = i + 1
            right = len(nums) - 1
            mid = 0 - nums[i]

            while left < right:
                if nums[left] + nums[right] == mid:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < mid:
                    left += 1
                else:
                    right -= 1
        return list(ans)