from data_structures.linked_list import linkedList

class HashMap:
    hashMapSize = 16

    def __init__(self):

        self.array = []

        for i in range(0, self.hashMapSize):
            self.array.append(linkedList())


    def add(self, input):

        hashNumber =  hash(input)

        print(hashNumber)
        index = hashNumber % self.hashMapSize
        print(index)

        self.array[index].add_node(input)


    @staticmethod
    def hash(input):
        hash = 0
        for c in input:
            hash = 101 * hash + ord(c)

        return hash


    def remove(self):
        NotImplemented


    def get(self):
        NotImplemented


    def __str__(self):
        output = ''

        for i in range(0, self.hashMapSize):
            # output = self.array[i].get_data()
            output += self.array[i].get_data()

        return output

test1 = 'asdf1234'
test2 = 'asdf1234'
test3 = 'asdf123'

print(id(test1))
print(id(test2))
print(id(test3))

hashmap = HashMap()

hashmap.add('hello')

print(hashmap)


hashmap.add('coolasdfawe')
hashmap.add('asd33faa3fa')
hashmap.add('q83578asdfasdfasd')
hashmap.add('aaa')

print(hashmap)


hashmap.add('aaa')
hashmap.add('aaa')
hashmap.add('aaa')