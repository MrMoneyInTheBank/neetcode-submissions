#include <unordered_map>
#include <vector>
class Solution {
public:
  std::vector<int> topKFrequent(std::vector<int> nums, int k) {
    std::unordered_map<int, int> freq;

    for (const int num : nums) {
      freq[num]++;
    }

    std::vector<std::vector<int>> buckets(nums.size(), std::vector<int>());

    for (const std::pair<const int, int> &kv : freq) {
      buckets[kv.second - 1].push_back(kv.first);
    }

    std::vector<int> res;

    for (int idx = buckets.size() - 1; idx >= 0; idx--) {
      if (res.size() == k)
        break;
      else if (buckets[idx].size() == 0)
        continue;
      else {
        res.insert(res.end(), buckets[idx].begin(), buckets[idx].end());
      }
    }

    return res;
  }
};
