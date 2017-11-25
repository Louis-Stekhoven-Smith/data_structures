# Linked list



# Node

class linkedList(object):



    def __init__(self):
        self.head = node()
        self.tail = self.head


    def add_node(self, val):
        self.tail.nextNode =  node(val)
        self.tail = self.tail.nextNode

    def remove_node(self, val):

        currentNode = self.head
        lastNode = currentNode

        while(currentNode):

            if(currentNode.val is val):
                currentNode.val = None
                lastNode.nextNode = currentNode.nextNode
                break

            lastNode = currentNode
            currentNode = currentNode.nextNode


class node():

    def __init__(self):
        self.nextNode = None
        self.val = None







