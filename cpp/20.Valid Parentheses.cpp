#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char>_stack;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '(' || s[i] == '[' || s[i] == '{'){
                _stack.push(s[i]);
            }
            else{
                if (_stack.empty())
                    return false;
                char pop_char = _stack.top();
                _stack.pop();
                if (s[i] == ')' && pop_char != '(')
                    return false;
                if (s[i] == ']' && pop_char != '[')
                    return false;
                if (s[i] == '}' && pop_char != '{')
                    return false;
            }
        }
        if (_stack.empty())
            return true;
        else
            return false;
    }
};

