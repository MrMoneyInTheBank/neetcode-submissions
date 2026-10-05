#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> nums, int target) {
    std::unordered_map<int, int> seen;

    for (int idx = 0; idx < nums.size(); idx++) {
      int comp = target - nums[idx];

      if (seen.contains(comp)) {
        return std::vector<int>{seen[comp], idx};
      } else {
        seen[nums[idx]] = idx;
      }
    }

    return std::vector<int>{};
  }
};
