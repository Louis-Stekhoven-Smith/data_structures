from data_structures.linked_list import linkedList

class HashMap:

    hashMapSize = 16

    def __init__(self):
        self.array = []
        for i in range(0, self.hashMapSize):
            self.array.append(linkedList())

    # TODO check if key already exists
    def add(self, key, input):
        hashNumber =  hash(key)
        index = hashNumber % self.hashMapSize
        self.array[index].add_node(hash, key, input)


    @staticmethod
    def hash(input):
        hash = 0
        for c in input:
            hash = 101 * hash + ord(c)

        return hash


    def remove(self):
        NotImplemented


    def get(self, key):
        NotImplemented


    def __str__(self):
        output = ''

        for i in range(0, self.hashMapSize):
            output += 'List '
            output += self.array[i].get_data()
            output += '\n'

        return output

hashmap = HashMap()

hashmap.add('aKey', '1234')

print(hashmap)


hashmap.add('another', '555')
hashmap.add('thisIsOne', 'data')
hashmap.add('test', 'more data')
hashmap.add('aaa', 'okies')
hashmap.add('aaa', 'yup')
hashmap.add('aaa', 'numnum')
hashmap.add('aaa', 'cool')


print(hashmap)