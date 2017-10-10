
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        for (int i=0;i<ransomNote.length();i++) {
        	String tmp=ransomNote.substring(i,i+1);
        	if(!magazine.contains(tmp)) 
        		return false;
        	else {
        		int j=magazine.indexOf(tmp);
        		magazine=magazine.substring(0,j)+magazine.substring(j+1);
        	}	
        }
        return true;
    }
}


public class _383_Ransom_Note {
	public static void main(String[] args) {
		Solution solution=new Solution();
		System.out.println(solution.canConstruct("fsdafas","sdfsafasdffsdafdassd"));
	}
}
