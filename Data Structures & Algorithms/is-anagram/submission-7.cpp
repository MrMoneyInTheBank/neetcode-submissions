#include <functional>

class Solution {
public:
    bool isAnagram(string s, string t) {
        function<vector<int>(string)> freq_array= [](string s) {
            vector<int> freq(26, 0);

            for (const char c : s) {
                int idx = c - 'a';
                freq[idx]++;
            }

            return freq;
        };

        return freq_array(s) == freq_array(t);        
    }
};
