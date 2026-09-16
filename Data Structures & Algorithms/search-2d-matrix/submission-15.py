class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lc, rc = 0, len(matrix) - 1
        lr, rr = 0, len(matrix[0]) - 1

        while lc <= rc:
            mc = (lc + rc) // 2
            if target < matrix[mc][lr]:
                rc = mc - 1

            elif target > matrix[mc][rr]:
                lc = mc + 1

            else:
                while lr <= rr:
                    mr = (lr + rr) // 2
                    if matrix[mc][mr] == target:
                        return True
                    
                    elif matrix[mc][mr] < target:
                        lr = mr + 1

                    elif matrix[mc][mr] > target:
                        rr = mr - 1

                return False
        return False
                    
                     
        
        



        