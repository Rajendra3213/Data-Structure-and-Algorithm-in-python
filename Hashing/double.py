class DoubleHashing:

    def __init__(self, size=14):
        self.size = size
        self.table = [None] * self.size
    
    def H1(self, value):
        return value % self.size
         
    def H2(self, value):
        return 1 + value % (self.size - 1)
    
    def H(self, value, i):
        return (self.H1(value) + i * self.H2(value)) % self.size
   
    def insert(self, value):
        i = 0
        key = self.H(value, i)
        while self.table[key] is not None:
            i += 1
            key = self.H(value, i)
        self.table[key] = value

    def retrieve(self, value):
        i = 0
        key = self.H(value, i)
        while self.table[key] is not None:
            if self.table[key] == value:
                # return the key where the value is found
                return key  
            i += 1
            key = self.H(value, i)
        return None
        
    def display(self):
        for key, value in enumerate(self.table):
                print(f'Index {key}: {value}')

elements = [12, 14, 2, 6, 9, 26]
hash_table = DoubleHashing(12)
for element in elements:
    hash_table.insert(element)
hash_table.display()
print(f'Retrieved Key for Value 2: {hash_table.retrieve(2)}')