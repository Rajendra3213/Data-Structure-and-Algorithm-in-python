class HuffmanTreeNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class HuffmanTree:
    def __init__(self, root=None):
        self.root = root

    def build_huffman_tree(self, s):
        # count the frequency of each character
        freq_map = {char:s.count(char) for char in s}
        
        huffman_tree = [HuffmanTreeNode(char, freq) for char, freq in freq_map.items()]
        
        # build Huffman Tree 
        while len(huffman_tree) > 1:
            # sort characters based on their frequencies in ascending order
            huffman_tree = sorted(huffman_tree, key=lambda x: x.freq)
            
            # pop the first two nodes 
            left = huffman_tree.pop(0)
            right = huffman_tree.pop(0)
            
            # merge the nodes
            merged_freq = left.freq + right.freq
            merged_node = HuffmanTreeNode(None, merged_freq)
            merged_node.add_left_child(left)
            merged_node.add_right_child(right)
            
            # add the merge node to the tree
            huffman_tree.append(merged_node)

        self.root = huffman_tree[0]

    def generate_codes(self, node=None, code="", huffman_code_map={}):
        if not node:
            node = self.root

        # if it's a leaf node, store the code
        if node.data:
            huffman_code_map[node.data] = code
            return huffman_code_map

        # traverse left and right
        self.generate_codes(node.left, code + "0", huffman_code_map)
        self.generate_codes(node.right, code + "1", huffman_code_map)

        return huffman_code_map
    
    def encode(self, s, huffman_codes):
        return ''.join([huffman_codes[char] for char in s])


# test huffman tree
s = "BCAADDDCCACACAC"
tree = HuffmanTree()
tree.build_huffman_tree(s)

# test huffman code
huffman_codes = tree.generate_codes()
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

# test encoding
encoded_string = tree.encode(s,huffman_codes)
print(f"Encoded string for '{s}': {encoded_string}")