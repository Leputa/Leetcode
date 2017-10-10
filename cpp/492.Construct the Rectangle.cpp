#include <vector>
#include <cmath>
using namespace std;


class Solution {
public:
    vector<int> constructRectangle(int area) {
        int a,b;
        for (int i=0;i<area;i++){
        	if(area%i==0&&area/i>=i){
        		a=area/i;
        		b=i;
			}
			if(area/i<i)
				break;
		}
		vector<int> rectangle;
		rectangle.push_back(a);
		rectangle.push_back(b);
		return rectangle;
    }
};


