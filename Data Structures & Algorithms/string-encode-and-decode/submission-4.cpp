#include <string>
#include <vector>

class Solution {
public:
  std::string encode(std::vector<std::string> strs) {
    std::string res = "";

    for (const std::string &s : strs) {
      res += std::to_string(s.length()) + '#' + s;
    }

    return res;
  }

  std::vector<std::string> decode(std::string s) {
    std::vector<std::string> res;
    int idx = 0;

    while (idx < s.length()) {
      int jdx = idx;
      int length = 0;

      while (s[jdx] != '#') {
        length = length * 10 + (s[jdx] - '0');
        jdx++;
      }

      std::string substring = s.substr(jdx + 1, length);
      idx = jdx + 1 + length;

      res.push_back(substring);
    }

    return res;
  }
};
