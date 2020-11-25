# encoding: utf-8
from collections import defaultdict

class DBTree(object):
    def __init__(self):
        self._root = DBNode(None, None)

    @property
    def root(self):
        return self._root
    
    def add(self, dbTransaction):
        currNode = self._root

        for item in dbTransaction:
            nextNode = currNode.searchChildren(item)

            if nextNode:
                nextNode.incrementCount()
            else:
                nextNode = DBNode(item)
                currNode.add(nextNode)
            
            currNode = nextNode

    def getSupportCount(self):
        result = defaultdict(lambda: 0)
        queue = []
        queue.append(self.root)

        while len(queue) != 0:
            node = queue.pop(0)

            if not node.item is None:
                result[node.item] += node.count

            for child in node.children:
                queue.append(node.children[child])
        
        return result

class DBNode(object):
    def __init__(self, item, count=1):
        self._item = item
        self._count = count
        self._parent = None
        self._children = {} # dictionary with key = the node item, and value = a DBNode
    
    @property
    def item(self):
        return self._item
    
    @property
    def count(self):
        return self._count

    @property
    def children(self):
        return self._children

    def add(self, childNode):
        if childNode._item not in self._children:
            self._children[childNode._item] = childNode
            childNode._parent = self
    
    def searchChildren(self, item):
        if item in self._children:
            return self._children[item]
        else:
            return None
    
    def incrementCount(self):
        self._count += 1

    def printNode(self):
        print("Item: %s\tCount: %d" % (self._item, self._count))

# Helper Functions
def getPaths(dbTree):
    result = []
    traverse(dbTree.root, result)
    return result

def traverse(node, paths, path = []):
    if not node.item is None:
        path.append(node.item)

    if len(node.children) == 0:
        temp = path[:]
        paths.append(temp)
        path.pop()
    else:
        for child in node.children:
            traverse(node.children[child], paths, path)
        
        if path:
            path.pop()
