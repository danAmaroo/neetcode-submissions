class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> dict;
        for( int& num : nums ){
            if (dict.count(num) == 0){
                dict[num] = 1;
            }
            else{
                return true;
            }
        }
        return false;

    }
};