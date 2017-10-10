#include <vector>
#include <string>
#include <sstream>
using namespace std;

template<typename T> string toString(const T& t){
    ostringstream oss;  //创建一个格式化输出流
    oss<<t;             //把值传递如流中
    return oss.str();   
}


class Solution {
public:
    vector<string> fizzBuzz(int n) {
    	vector<string>ans;
        for (int i=1;i<=n;i++){
        	if (i%3!=0&&i%5!=0)
        		ans.push_back(toString(i));
        	else if (i%3==0&&i%5==0)
        		ans.push_back("FizzBuzz");
        	else if (i%3==0)
        		ans.push_back("Fizz");
        	else if (i%5==0)
        		ans.push_back("Buzz");
		}
		return ans;
    }
};
