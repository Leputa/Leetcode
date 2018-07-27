import java.sql.ResultSet;

public class _260_Single_Number_III_ {
    public int[] singleNumber(int[] nums) {
        int tmp = 0;
        for (int num: nums)
        	tmp ^= num;
        
        int flag = 1;
        for (int i=0; i<32; i++) {
        	if (((flag<<i)&tmp) != 0) {
        		flag = flag<<i;
        		break;
        	}
        }
        int [] results = new int[2];
        int res1 = 0, res2 = 0;
        for (int num: nums) {
        	if ((num&flag) == 0)
        		res1 ^= num;
        	else
        		res2 ^= num;
        }
        results[0] = res1; 
        results[1] = res2;
        return results;
    }
    
    public static void main(String[] args) {
		int[] nums = {1,2,1,3,2,5};
		
		_260_Single_Number_III_ solution = new _260_Single_Number_III_();
		int[] results = solution.singleNumber(nums);
		for (int result: results) {
			System.out.println(result);
		}
	}
}
