import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class _609_Find_Duplicate_File_in_System {
	public List<List<String>> findDuplicate(String[] paths) {
		List<List<String>>ans=new ArrayList<List<String>>();
		int len=paths.length;
		
		if(len==0)
			return ans;
		
		Map<String, Set<String>>map=new HashMap<>();
		
		for (String path:paths) {
			String[]strs=path.split("\\s+"); //"\\s"表示空格，"\\s+"表示多个空格
			for(int i=1;i<strs.length;i++) {
				int index=strs[i].indexOf("(");
				String content=strs[i].substring(index, strs[i].length()-1);
				String file=strs[0]+"/"+strs[i].substring(0, index);
				Set<String>filesname=map.getOrDefault(content, new HashSet<String>());
				filesname.add(file);
				map.put(content,filesname);
			}
		}
		for (String key:map.keySet()) {
			if(map.get(key).size()>1)
				ans.add(new ArrayList<String>(map.get(key)));
		}
		
		return ans;
    }

}
