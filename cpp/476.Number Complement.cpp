#include <cmath> 

class Solution {
public:
    int findComplement(int num) {
    	int binary[35];
    	int i=0;
        while(num!=0){
        	binary[i]=num%2;
        	num/=2;
        	i++;
		}
		for(int j=0;j<i;j++){
			if(binary[j]==1)
				binary[j]=0;
			else
				binary[j]=1;
		}
		int ans=0;
		for(int j=0;j<i;j++)
			ans+=binary[j]*pow(2,j);
		return ans;
    }
};
