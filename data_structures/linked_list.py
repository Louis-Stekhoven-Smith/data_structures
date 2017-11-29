# Linked list



# Node

class linkedList(object):


    def __init__(self, val = None):

        if(val is not None):
            self.head = node(val)

        else:
            self.head = None

        self.tail = self.head

    # Add new node to the end of the list
    def add_node(self, val):

        if(self.head is None):
            self.head = node(val)
            self.tail = self.head

        else:
            self.tail.nextNode =  node(val)
            self.tail = self.tail.nextNode


    # Removes node with given val
    def remove_node(self, val):

        currentNode = self.head
        lastNode = currentNode

        while(currentNode):

            # Removes node unless
            if(currentNode.val is val):

                currentNode.val = None

                # If the node being removed is the head of the list reset head to next node
                if(currentNode is lastNode):
                    self.head = currentNode.nextNode
                    break

                # Remove node
                else:
                    lastNode.nextNode = currentNode.nextNode
                    break


            lastNode = currentNode
            currentNode = currentNode.nextNode


    def get_data(self):
        content = ''
        currentNode = self.head

        if (currentNode is None):
            return ''

        # How you do a do while loop in python
        # There is no do while in python
        while (True):
            content += (currentNode.val)
            content += '\n'
            currentNode = currentNode.nextNode

            if (currentNode is None):
                break

        return content


    def __str__(self):
        content = ''
        currentNode = self.head

        if(currentNode is None):
            return ''

        # How you do a do while loop in python
        # There is no do while in python
        while (True):
            content += (currentNode.val)
            content += '\n'
            currentNode = currentNode.nextNode

            if(currentNode is None):
                break

        return content


class node(object):

    def __init__(self,val):
        self.nextNode = None
        self.val = val


'''

list = linkedList()

list.add_node('First')

print(list)

list.add_node('Second')
list.add_node('Third')
list.add_node('Fourth')

print(list)

list.remove_node('Second')

print(list)

list.remove_node('Head')

print(list)

list.remove_node('Fourth')

print(list)

list.remove_node('doesnt exist')

print(list)

list.remove_node('First')
list.remove_node('Third')

print(list)

list.add_node('Fourth')
'''






