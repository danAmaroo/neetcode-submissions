class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, total):
            if total == target: # find target
                res.append(curr.copy())
                return 
            if i >= len(nums) or total >target: # no solution down this path
                return 

            curr.append(nums[i]) # include same candidate
            dfs(i, curr, total + nums[i])

            curr.pop() # don't include new candidate
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


        