#include <string>
#include <vector>
using namespace std;

bool comp(const int &a, const int &b){
    int _a = a, _b=b;
    vector<int>vec_a,vec_b;
    while(_a){
        vec_a.push_back(_a%10);
        _a /= 10;
    }
    while(_b){
        vec_b.push_back(_b%10);
        _b /= 10;
    }
    int i=vec_a.size()-1, j=vec_b.size()-1;
    while(i>=0 && j>=0){
        if (vec_a[i] < vec_b[j])  return true;
        if (vec_a[i] > vec_b[j])  return false;
        i--;
        j--;
    }
    while (i>=0){
        if (vec_a[i] < vec_a[i+1]) return true;
        if (vec_a[i] > vec_a[i+1]) return false;
        if (vec_a[i] == vec_a[i+1]) i--; 
    }
    while (j>=0){
        if (vec_b[j] < vec_b[j+1]) return false;
        if (vec_b[j] > vec_b[j+1]) return true;
        if (vec_b[j] == vec_b[j+1]) j--;
    }
    return true;
} 

class Solution {
public:

    string PrintMinNumber(vector<int> numbers) {
        sort(numbers.begin(), numbers.end(), comp);
        string ret;
        for (auto num: numbers){
            string tmp = to_string(num);
            ret += tmp;
        }
        return ret;
    }
};