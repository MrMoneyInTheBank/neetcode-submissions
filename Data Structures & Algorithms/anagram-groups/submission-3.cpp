#include <functional>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

struct VectorHash {
    size_t operator()(const vector<int>& v) const {
        size_t h = 0;
        for (const int x : v) {
            h ^= hash<int>{}(x) + 0x9e3779b9 + (h << 6) + (h >> 2);
        }
        return h;
    }
};

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        function<vector<int>(const string&)> encode = [](const string& s) -> vector<int> {
            vector<int> res(26, 0);
            for (const char c : s) {
                res[c - 'a']++;
            }
            return res;
        };

        unordered_map<vector<int>, vector<string>, VectorHash> groups;

        for (const string& s : strs) {
            groups[encode(s)].push_back(s);
        }

        vector<vector<string>> res;
        res.reserve(groups.size());
        for (pair<const vector<int>, vector<string>>& kv : groups) {
            res.push_back(move(kv.second));
        }

        return res;
    }
};