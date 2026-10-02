#include <string>
#include <unordered_map>

class Solution {
public:
    std::unordered_map<char, int> freq(std::string s) {
        std::unordered_map<char, int> res;

        for (const char c : s) {
            res[c]++;
        }

        return res;
    }

    bool isAnagram(string s, string t) {
        return freq(s) == freq(t);
    }
};
