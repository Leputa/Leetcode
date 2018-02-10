class MyCalendar:

    def __init__(self):
    	self.Calendar=[]
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        tag=0
        for book in self.Calendar:
        	if (start>=book[0] and start<book[1]) or (end>book[0] and end<=book[1]) or (start<book[0] and end>book[1]):
        		tag=1
        		break
        if tag==1:
        	return False
        else:
        	self.Calendar.append([start,end])
        	return True

     