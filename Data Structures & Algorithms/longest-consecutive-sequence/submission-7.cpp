#include <unordered_set>
#include <vector>
class Solution {
public:
  int longestConsecutive(std::vector<int> nums) {
    if (nums.size() == 0)
      return 0;

    std::unordered_set<int> numSet(nums.begin(), nums.end());
    int res = 1;

    for (int num : nums) {
      if (numSet.contains(num - 1))
        continue;
      else {
        int curr = 1;

        while (numSet.contains(num + 1)) {
          curr++;
          num++;
        }

        res = std::max(res, curr);
      }
    }

    return res;
  }
};
