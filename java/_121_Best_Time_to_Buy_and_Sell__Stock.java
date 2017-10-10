
public class _121_Best_Time_to_Buy_and_Sell__Stock {
	public int maxProfit(int[] prices) {
		if (prices.length==0)
			return 0;
        int profit=0;
        int head=prices[0];
        int tail=0;
        int tagh=0;
        int tagt=0;
        for(int i=1;i<prices.length;i++) {
        	if(prices[i]>prices[i-1]) {
        		tail=prices[i];
        		tagt=i;
        	}
        		
        	else {
        		head=min(head,prices[i]);
        		if(head==prices[i])
        			tagh=i;
        	}
        	if(tail-head>profit&&tail!=0&&tagh<tagt)
    			profit=tail-head;
        }	
        return profit;
    }
	private int min(int a,int b) {
		return a<b?a:b;
	}	
}
