class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> set;
        for(int i = 0; i < nums.size(); i++){
            if(set.find(nums[i]) != set.end()){
                return true;
                
            }
            else{
                set.insert(nums[i]);
            }
        }
        return false;
    }
};
