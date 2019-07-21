#include <string>
#include <unordered_map>
using  namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int>map;
        unordered_map<int, int>::iterator it;
        int max_length = 0;
        int start = 0;
        for (int i = 0; i<s.size(); i++){
            if (map.find(s[i]) != map.end())
                start = max(start, map[s[i]] + 1);
            max_length = max(max_length, i-start+1);
            map[s[i]] = i;
        }
        return max_length;
    }
};