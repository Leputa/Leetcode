import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Interval {
	int start;
	int end;
	Interval() { start = 0; end = 0; }
	Interval(int s, int e) { start = s; end = e; }
}



/*public class _436_Find_Right_Interval {
	class Node implements Comparable<Node>{
		public Interval interval;
		public int index;
		Node(Interval interval,int index){
			this.interval=interval;
			this.index=index;
		}
		public int compareTo(Node o){
			Node s=(Node) o;
			if (this.interval.start<s.interval.start)
				return -1;
			else
				return 1;
		}
	}
	
    public int[] findRightInterval(Interval[] intervals) {
        int n=intervals.length;
        int[]ans=new int[n];
        if(n==0)
        	return ans;
        List<Node>list=new LinkedList<>();
        for(int i=0;i<n;i++){
        	Node tmpNode=new Node(intervals[i],i);
        	list.add(tmpNode);
        }
        Collections.sort(list);
        
        for (int i=0;i<n-1;i++){
        	int tag=0;
        	for(int j=i+1;j<n;j++){
        		if (list.get(i).interval.end<=list.get(j).interval.start){
            		ans[list.get(i).index]=list.get(j).index;
            		tag=1;
            		break;
            	}
        	}
        	if (tag==0)
        		ans[list.get(i).index]=-1;
        }
        ans[list.get(n-1).index]=-1;
        return ans;
    }
}*/

//*****************上述解法超时******************//

public class _436_Find_Right_Interval{
	public int[] findRightInterval(Interval[] intervals) {
        int n=intervals.length;
        int[]ans=new int[n];
        if(n==0)
        	return ans;
		TreeMap<Integer, Integer>intervalMap=new TreeMap<>();
		for (int i=0;i<n;i++)
			intervalMap.put(intervals[i].start, i);
		for (int i=0;i<n;i++){
			Map.Entry<Integer, Integer>entry=intervalMap.ceilingEntry(intervals[i].end);
			ans[i]=(entry!=null)?entry.getValue():-1;
		}
		return ans;
	}
}


