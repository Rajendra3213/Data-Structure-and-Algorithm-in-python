# Replace ___ with your code

class ChainingHashTable:

    def __init__(self, size=14):
        self.size = size
        self.table = [None] * self.size

    H = lambda self, value: value % self.size

    def insert(self, value):
        key = self.H(value)
        if (self.table[key] is None):
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            self.table[key] = sorted(self.table[key])
        

    def display(self):
        for key, value_list in enumerate(self.table):
            print(f'{key}: {value_list}')

elements = [10, 15, 17, 3, 20, 16, 5]
hash_table = ChainingHashTable()
for element in elements:
    hash_table.insert(element)

hash_table.display()