
public class _309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown {
    public int maxProfit(int[] prices) {
    	int len=prices.length;
        if (len<2)
        	return 0;
        int[]sell=new int[len];   //���������δ�ֹ�״̬
        int[]buy=new int[len];    //���������ֹ�״̬
        
        buy[0]=-prices[0];
    	sell[1]=Math.max(sell[0], buy[0]+prices[1]);   
    	buy[1]=Math.max(buy[0],0-prices[1]);
    	
        for (int i=2;i<len;i++){
        	sell[i]=Math.max(sell[i-1], buy[i-1]+prices[i]);   //max{(ǰһ��Ҳδ�ֹɵ��������),(ǰһ��ֹɣ������������������)}
        	buy[i]=Math.max(buy[i-1],sell[i-2]-prices[i]);      //max{(ǰһ��ֹ��������),(ǰ��������������������������)}
        }
        return sell[len-1];
    }
}
