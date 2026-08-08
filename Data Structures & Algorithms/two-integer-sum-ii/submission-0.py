class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            diff = numbers[j] + numbers[i]
            if diff == target:
                break
            if diff < target:
                i += 1
            else:
                j -= 1
        
        return [i + 1, j + 1]