class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = 1
        curr = 1
        max_total = 1
        if len(nums) == 0:
            return 0
        while(r < len(nums)):
            if nums[r] == nums[r-1]:
                r += 1
                continue
            elif nums[r] == nums[r-1] + 1:
                curr += 1
                max_total = max(max_total, curr)
            else:
                curr = 1
                l = r

            r += 1
        return max_total 
