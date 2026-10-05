class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int idx = 0; idx < nums.size(); idx++) {
            int comp = target - nums[idx];

            if (seen.contains(comp)) {
                return vector<int>{seen[comp], idx};
            }
            seen[nums[idx]] = idx;
        }
    }
};
