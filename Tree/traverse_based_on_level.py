# create a class to handle the creation of node and addition of child nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# class to handle the creation of trees and operations performed in it
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_nodes_at_k(self,node, k):
        if node is None:
            return []
        elif k == 0:
            return [node.data]
        else:
            result = []
            for child in node.children:
                result += self.get_nodes_at_k(child, k - 1)
            return result

# creating our root node
root = TreeNode("Book")

# creating the children of root
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)

# creating our leaf nodes
child1_1 = TreeNode(1.1)
child1_2 = TreeNode(1.2)
child1_3 = TreeNode(1.3)
child1_4 = TreeNode(1.4)
child2_1 = TreeNode(2.1)
child3_1 = TreeNode(3.1)
child3_2 = TreeNode(3.2)
child3_3 = TreeNode(3.3)

# describing relationships between the nodes

# add children to the root node
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# add children to child1
child1.add_child(child1_1)
child1.add_child(child1_2)
child1.add_child(child1_3)
child1.add_child(child1_4)

# add children to child2
child2.add_child(child2_1)

# add children to child3
child3.add_child(child3_1)
child3.add_child(child3_2)
child3.add_child(child3_3)

# creating our tree
tree = Tree(root)
for i in range(0,3):
    print(f"nodes at depth {i}: {tree.get_nodes_at_k(root, i)}")