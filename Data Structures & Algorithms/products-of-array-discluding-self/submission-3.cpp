#include <vector>
class Solution {
public:
  std::vector<int> productExceptSelf(std::vector<int> nums) {
    std::vector<int> output(nums.size(), 1);
    int runningProduct = nums[0];

    for (int idx = 1; idx < output.size(); idx++) {
      output[idx] = runningProduct;
      runningProduct *= nums[idx];
    }

    runningProduct = nums[nums.size() - 1];

    for (int idx = nums.size() - 2; idx >= 0; idx--) {
      output[idx] *= runningProduct;
      runningProduct *= nums[idx];
    }

    return output;
  }
};
