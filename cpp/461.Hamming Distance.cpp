#include <iostream>
using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
    	int ans=0;
    	int a[32]={0},b[32]={0};
    	int i=31;
    	while(x!=0){
    		a[i]=x%2;
    		x=x/2;
    		i--;
		}
		i=31;
		while(y!=0){
			b[i]=y%2;
			y/=2;
			i--;
		}
		for(int i=0;i<32;i++)
			if(a[i]!=b[i])
				ans++;
		return ans;
    }
};

int main(){
	int x,y;
	int ans;
	cin>>x>>y;
	Solution s;
	ans=s.hammingDistance(x,y);
	cout<<ans<<endl;
	return 0;
}
