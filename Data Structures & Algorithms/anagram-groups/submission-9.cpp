#include <string>
#include <unordered_map>
#include <vector>

class Solution {
private:
  std::string encode(const std::string &s) {
    std::vector<int> freq(26, 0);

    for (const char c : s) {
      freq[c - 'a']++;
    }

    std::string key;

    for (const int f : freq) {
      key += f + '#';
    }

    return key;
  }

public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> strs) {
    std::unordered_map<std::string, std::vector<std::string>> groups;

    for (const std::string &s : strs) {
      std::string key = encode(s);
      groups[key].push_back(s);
    }

    std::vector<std::vector<std::string>> res;

    for (const auto &kv : groups) {
      res.push_back(kv.second);
    }

    return res;
  }
};
