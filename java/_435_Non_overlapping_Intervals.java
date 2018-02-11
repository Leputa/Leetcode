import java.util.Collections;
import java.util.LinkedList;
import java.util.List;


public class _435_Non_overlapping_Intervals {
	class Node implements Comparable<Node>{
		public Interval interval;
		
		Node(Interval interval){
			this.interval=interval;
		}
		
		public int compareTo(Node o){
			Node s=(Node) o;
			if (this.interval.end<s.interval.end)
				return -1;
			else if(this.interval.end==s.interval.end){
				if (this.interval.start<s.interval.start)
					return -1;
				else
					return 1;
			}
			else 
				return 1;
		}
	}
		
    public int eraseOverlapIntervals(Interval[] intervals) {
        int n=intervals.length;
        int ans=0;
        if(n==0)
        	return ans; 
        List<Node>list=new LinkedList<>();
        for (int i=0;i<n;i++)
        	list.add(new Node(intervals[i]));
        Collections.sort(list);
        int end=list.get(0).interval.end;
        for (int i=1;i<n;i++){
        	if (list.get(i).interval.start<end)
        		ans+=1;
        	else
        		end=list.get(i).interval.end;
        }	
        return ans;
    }
}
