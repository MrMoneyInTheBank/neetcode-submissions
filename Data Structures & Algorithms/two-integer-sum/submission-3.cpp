class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int comp = target - num;
            if (seen.find(comp) != seen.end()) {
                return {seen[comp], i};
            }
            seen[num] = i;
        }
    }
};
