class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            # new sum = -nums[i]
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res = [nums[i], nums[l], nums[r]]
                    res.sort()
                    if res not in ans:
                        ans.append(res)
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1


        return ans
                    
                    


            




        