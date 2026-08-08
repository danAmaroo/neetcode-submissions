class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int n = nums.size();
        vector<int> answer;
        for(int i = 0; i < n; i++){
        int value = target - nums[i];
        if (map.count(value)){
            if(map[value] < i){
                return answer = {map[value], i};
            }
            else{
                return answer = {i, map[value]};
            }

        }
        else{
            map[nums[i]] = i;
        }
        }
    }
};
