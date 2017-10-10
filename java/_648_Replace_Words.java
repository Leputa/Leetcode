import java.util.List;

public class _648_Replace_Words {
    public String replaceWords(List<String> dict, String sentence) {
        String[]tmpString=sentence.split(" ");
        StringBuilder[]stringBuilders=new StringBuilder[tmpString.length];
        for(int i=0;i<tmpString.length;i++) {
        	stringBuilders[i]=new StringBuilder(tmpString[i]);
        	for(int j=0;j<dict.size();j++) {
        		String dic=dict.get(j);
        		int length=dic.length();
        		if(length>=tmpString[i].length())
        			continue;
        		String tmp=new String(stringBuilders[i].substring(0,length));
        		if (tmp.equals(dic)){
        			stringBuilders[i]=new StringBuilder(dic);
        			break;
        		}
        	}
        }
        
        String ans=new String();
        for (int i=0;i<tmpString.length-1;i++) {
        	ans+=new String(stringBuilders[i])+" ";
        }
        ans+=new String(stringBuilders[tmpString.length-1]);
        return ans;
    }
}
