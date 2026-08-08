class Solution {
public:
    bool hasDuplicate(vector<int>& nums1) {
        unordered_map<int, int> nums;
        bool flag = false;
        for(int i = 0; i < nums1.size();i++){
            if (nums.count(nums1[i]) == 1)
            {
                flag = true;
            }
            else
            {
                nums[nums1[i]] = 1;
            }
        }
        return flag;
    }
};
