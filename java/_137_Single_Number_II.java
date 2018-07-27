
public class _137_Single_Number_II {
    public int singleNumber(int[] nums) {
        int[] flags = new int[32];
        for (int i=0; i<32; i++) {
        	for (int num: nums) {
        		flags[i] += (num>>i)&1;
        		flags[i] %= 3;
        	}
        }
        int result = 0;
        for (int i=0; i<32; i++) { 
        	// 需要仔细想一下为什么补码这样定义
        	result += (flags[i] << i);               
        	//result += Math.pow(2, i)*flags[i];    //这样写遇到负数有问题
        }
        return result;
    }
    
    public static void main(String[] args) {
		int[] nums = {2,2,-4,2};
		_137_Single_Number_II solution = new _137_Single_Number_II();
		System.out.println(solution.singleNumber(nums));
	}
}
