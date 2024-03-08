# Replace ___ with your code

class ModulusHashing:
    # creation
    def __init__(self):
        self.table = [None] * 10

    def find_load_factor(self):
    # occupied slot/total slots
        occupied_slots = sum(1 for slot in self.table if slot is not None)
        return occupied_slots / len(self.table)

    # modulus hash function
    def H(self, key):
        # equal to key % size(10)
        return key % 10

    # insert
    def insert(self, data):
        # hash value
        hash_value = self.H(data)
        # insert to table
        self.table[hash_value] = data
        # check if load factor exceeds after each insertion
        if self.find_load_factor() > 0.5:
            self.rehash()
    
    # rehash
    def rehash(self):
        # write your code here
        new_size = 2 * len(self.table)
        new_table = [None] * new_size
        for data in self.table:
            if data is not None:
                hash_value = data % new_size
                new_table[hash_value] = data
        
        self.table = new_table
        

        

    # display table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
# create a hash table with the given elements
elements = [1, 3, 5, 4, 7, 2, 9, 20]
hash_table = ModulusHashing()
for element in elements:
    hash_table.insert(element)

# display the hash table
hash_table.display()