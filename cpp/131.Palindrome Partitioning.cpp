#include <vector>
#include <string>
using namespace std;


class Solution {
private:
    vector<vector<string>> ret;

    bool isPalindrome(string s){
        int low = 0;
        int high = s.length() - 1;
        while(low < high){
            if (s[low] != s[high])
                return false;
            ++low;
            --high;
        }
        return true;
    }
    void trace_back(string s, vector<string> tmpVector, int length){
        int sum_length = 0;
        for (auto str: tmpVector){
            sum_length += str.length();
        }
        if (sum_length == length){
            vector<string>vec(tmpVector);
            ret.push_back(vec);
        }
        for (int i=0; i<s.length(); i++){
            string s1;
            s1.assign(s, 0, i+1);
            if (isPalindrome(s1)){
                tmpVector.push_back(s1);
                string s2;
                s2.assign(s, i+1, s.length()-(i+1));
                trace_back(s2, tmpVector, length);
                tmpVector.pop_back();
            }
        }
    }


public:
    vector<vector<string>> partition(string s) {
        vector<string>tmpVector;
        trace_back(s, tmpVector, s.length());
        return ret;
    }
};
