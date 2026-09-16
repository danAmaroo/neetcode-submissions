class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(piles) <= h

        # k <= max(piles)

        # TRICK -> brute force+ approach
        # create array of all possible k
        # binary search on k to try and see if it works

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p)/ k) # 4 / 2 = 2, 3 / 2 = 2
            
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

            




         