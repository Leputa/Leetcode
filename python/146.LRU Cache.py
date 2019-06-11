class Node():
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()  #key to Node
        self.headNode = Node(-1, -1)
        self.tailNode = Node(-1, -1)
        self.headNode.next = self.tailNode
        self.tailNode.pre = self.headNode
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        visitNode = self.map[key]
        self.move2tail(visitNode)
        return visitNode.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            putNode = self.map[key]
            putNode.val = value
            self.move2tail(putNode)
        else:
            if len(self.map) == self.capacity:
                self.remove()
            insertNode = Node(key, value)
            insertNode.next = self.tailNode
            insertNode.pre = self.tailNode.pre
            self.tailNode.pre.next = insertNode
            self.tailNode.pre = insertNode
            self.map[key] = insertNode
            assert len(self.map) <= self.capacity

    def remove(self):
        removeNode = self.headNode.next
        self.headNode.next = removeNode.next
        removeNode.next.pre = self.headNode
        removeNode.next = None
        removeNode.pre = None
        key = removeNode.key
        del self.map[key]
        del removeNode

    def move2tail(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.next = self.tailNode
        node.pre = self.tailNode.pre
        self.tailNode.pre.next = node
        self.tailNode.pre = node


if __name__ == '__main__':
    c = LRUCache(1)
    c.put(3, 4)
    c.put(2, 1)
    c.put(5, 6)


