class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        auto encode = [](string s) {
            vector<int> freq(26, 0);
            string res;

            for (const char c : s) {
                freq[c - 'a']++;
            }

            for (const int f : freq) {
                res += to_string(f) + '#';
            }

            return res;
        };

        unordered_map<string, vector<string>> groups;
        for (const string& s : strs) {
            string key = encode(s);
            groups[key].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& kv : groups) {
            res.push_back(kv.second);
        }

        return res;
    }
};
