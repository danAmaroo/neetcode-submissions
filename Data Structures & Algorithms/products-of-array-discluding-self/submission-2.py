class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
                continue
            total *= num
        
        ans = []
        for num in nums:
            if zero > 1:
                ans.append(0)
            elif zero > 0 and num != 0:
                ans.append(0)
            elif zero:
                ans.append(total)
            else:
                ans.append(int(total / num))
        
        return ans
