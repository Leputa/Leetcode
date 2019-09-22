#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    int LastRemaining_Solution(int n, int m)
    {
        if (n==0)
            return -1;
        vector<bool>flags(n, false);
        int cnt = 0;
        int pos = 0;
        while(cnt != n-1){
            int i = 0, cur = 0; 
            while(cur < m){
                if (!flags[(pos+i)%n])
                    cur++;
                ++i;
            }
            --i;
            pos = (pos+i) % n;
            flags[pos] = true;
            ++cnt;
        }
        for (int i=0; i<flags.size(); i++)
            if (!flags[i]) return i;
    }
};

int main(){
    Solution solution = Solution();
    cout << solution.LastRemaining_Solution(6, 5) << endl;
    return 0;
}

