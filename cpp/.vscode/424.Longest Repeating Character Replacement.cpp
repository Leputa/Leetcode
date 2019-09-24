#include <string>
#include <map>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = 0;
        map<char, int>_map;
        int ret = 0;
        for (right = 0; right < s.length(); right++){
            _map[s[right]]++;
            int max_val = 0;
            char key;
            for (map<char, int>::iterator iter = _map.begin(); iter != _map.end(); iter++){
                if (iter->second > max_val){
                    max_val = iter->second;
                    key = iter->first;
                }
            }
            if (right - left + 1 - max_val > k){
                _map[s[left]]--;
                left += 1;
            }else{
                ret = max(ret, right-left+1);
            }
        }
        return ret;
    }
};