# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

import queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """ 
        ret = []
        if root == None:
        	return ret
        q = queue.Queue()
        q.put(root)

        while(not q.empty()):
        	length = q.qsize()
        	tmp_list = []
        	for i in range(length, 0, -1):
        		node = q.get()
        		tmp_list.append(node.val)
        		for child in node.children:
        			q.put(child)
        	ret.append(tmp_list)
        return ret
