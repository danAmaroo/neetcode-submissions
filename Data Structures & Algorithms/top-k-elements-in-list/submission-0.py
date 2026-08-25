class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        freq_list = list(freq.items())
        freq_list.sort(key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(0, k):
            ans.append(freq_list[i][0])
        return ans

            


        
        

            
            


