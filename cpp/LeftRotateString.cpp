#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string LeftRotateString(string str, int n) {
        string ret;
        int length = str.length();
        if (length < n)
            return ret;
        str += str;
        // ret.assign(str, n, n+length);
        ret = str.substr(n, length);
        return ret;
    }
};

int main(){
    string str = "XYZdefabc";
    int n = 20;
    Solution solution = Solution();
    cout << solution.LeftRotateString(str, n) << endl;
    return 0;
}