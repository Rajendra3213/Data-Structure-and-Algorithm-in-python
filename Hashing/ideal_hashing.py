# Replace ___ with your code

class IdealHashing:
    # creation
    def __init__(self):
        self.table = [None] * 10

    # ideal hash function
    def H(self, key):
        # write your code here
        return key

    # insert
    def insert(self, data):
        # write your code here
        value = self.H(data)
        self.table[data] = value

    # display table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
# create a hash table with the given elements
elements = [1, 3, 5, 4, 7, 2, 9]
hash_table = IdealHashing()
for element in elements:
    hash_table.insert(element)

# display the hash table
hash_table.display()