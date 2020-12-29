class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):  
		array.append(self.name)
		for ele in self.children:
			ele.depthFirstSearch(array)			
		return array
			