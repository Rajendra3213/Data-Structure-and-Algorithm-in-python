# Replace ___ with your code

# a class to create and add nodes
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    def add_child(self,data):
        self.children.append(data)
    
# a class to create a tree and perform tree operations
class Tree:
    def __init__(self,root=None):
        self.root = root
    
    def get_nodes_at_depth(self,node,depth):
        if not node:
            return 
        if depth == 0:
            return node.data
        if node and depth >0:
            result = 0
            for child in node.children:
                result+=self.get_nodes_at_depth(child,depth-1)
            return result

# create the root node
root = TreeNode('root')

# create leaf nodes
child1 = TreeNode(1)
child1_1 = TreeNode(2)
child1_1_1 = TreeNode(3)

# describe relationships between the nodes
root.add_child(child1)
child1.add_child(child1_1)
child1_1.add_child(child1_1_1)

# create the tree
tree = Tree(root)

# get nodes at each level
for i in range(0,4):
    print(f"Nodes at Level {i}: {tree.get_nodes_at_depth(root, i)}")
