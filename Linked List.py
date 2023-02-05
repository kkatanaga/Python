from operator import itemgetter

class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class List:
    def __init__(self):
        self.head = None

def openList(list):
    return list.head

def printList(list):
    node = openList(list)
    while node is not None:
        print(node.item)
        node = node.next
    
list = List()
list.head = Node(1)
list.head.next = Node(2)
list.head.next.next = Node(3)
printList(list)