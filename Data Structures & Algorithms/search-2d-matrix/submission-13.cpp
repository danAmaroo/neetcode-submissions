class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size() - 1, t(0);
        if (matrix[0][0] == target) {return true;}

        while(l <= r){
            int m = (l+r) / 2;
            if(matrix[m][0] > target)
            {
                r = m -1;
            }
            else if(matrix[m][matrix[m].size()-1] < target)
            {
                l = m + 1;
            }
            else
            {
                t = m;
                break;
            }
        }

        r = matrix[0].size();
        l = 0;

        while(l <= r)
        {
            int m = (l+r) / 2;
             if(matrix[t][m] > target)
            {
                r = m - 1;
            }
            else if(matrix[t][m] < target){
                l = m + 1;
            }
            else{
                return true;
            }
        }
    return false;
    }
};
