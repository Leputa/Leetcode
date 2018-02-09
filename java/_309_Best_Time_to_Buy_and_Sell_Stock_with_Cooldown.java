
public class _309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown {
    public int maxProfit(int[] prices) {
    	int len=prices.length;
        if (len<2)
        	return 0;
        int[]sell=new int[len];   //当天操作后未持股状态
        int[]buy=new int[len];    //当天操作后持股状态
        
        buy[0]=-prices[0];
    	sell[1]=Math.max(sell[0], buy[0]+prices[1]);   
    	buy[1]=Math.max(buy[0],0-prices[1]);
    	
        for (int i=2;i<len;i++){
        	sell[i]=Math.max(sell[i-1], buy[i-1]+prices[i]);   //max{(前一天也未持股的最大利益),(前一天持股，当天卖出的最大利益)}
        	buy[i]=Math.max(buy[i-1],sell[i-2]-prices[i]);      //max{(前一天持股最大利益),(前两天卖出，当天买入的最大利益)}
        }
        return sell[len-1];
    }
}
