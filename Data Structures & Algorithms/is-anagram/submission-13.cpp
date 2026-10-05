#include <algorithm>
#include <string>
#include <vector>
class Solution {
public:
  bool isAnagram(std::string s, std::string t) {
    std::vector<int> freq(26, 0);

    for (const char c : s) {
      freq[c - 'a']++;
    }

    for (const char c : t) {
      freq[c - 'a']--;
    }

    return std::count(freq.begin(), freq.end(), 0) == freq.size();
  }
};
