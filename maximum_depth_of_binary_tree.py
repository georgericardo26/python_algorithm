"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

maximum depth of a tree = maximum number of nodes

https://www.geeksforgeeks.org/binary-tree-data-structure/

https://www.tutorialspoint.com/maximum-depth-of-binary-tree-in-python

m = 2ˆl
l = number of nodes
root => l =0, number of node is 2ˆ0 = 1

if the number of nodes is 2ˆl, so the next level is: 2 * 2ˆl

Number of nodes in a binary tree of height 'h' is 2^h - 1.
height of a tree = number of nodes from root to leaf path

height of a tree with a single node is considered as 1
A tree has maximum nodes if all levels have maximum nodes.

maximum number of nodes in a binary tree of height h is 1 + 2 + 4 +..+2^(h+1) - 1

L = T + 1
L = Number of leaf nodes
T = Number of internal nodes with two children


Types of Binary Tree

1. Full Binary Tree
    A Binary tree is a full binary tree if every node has 0 or 2 children
    In a Full Binary Tree, number of leaf nodes is the number of internal nodes plus 1
       L = I + 1
    Where L = Number of leaf nodes, I = Number of internal nodes

2. Complete Binary Tree: A Binary Tree is a complete Binary Tree if all the levels are completely filled except
possibly the last level and the last level has all keys as left as possible

3. Perfect Binary Tree: A Binary tree is a Perfect Binary Tree in wich all the internal nodes have two children and all
leaf nodes are at the same level.

    A Perfect Binary Tree of height h (where the height of the binary tree is the longest path from the root node to
    any leaf node in the tree) has 2h+1 – 1 node.

4. Balanced Binary Tree
    A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes

5. A degenerate (or pathological) tree:
    A Tree where every internal node has one child. Such trees are performance-wise same as linked list.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#
# def max_depth(node):
#     if node is None:
#         return 0
#     else:
#         lDepth = max_depth(node.left)
#         rDepth = max_depth(node.right)
#
#         if lDepth > rDepth:
#             return lDepth + 1
#         else:
#             return rDepth + 1


def max_depth(node):

    if node is None:
        return 0

    l_depth = max_depth(node.left)
    r_depth = max_depth(node.right)

    if l_depth > r_depth:
        return l_depth + 1

    return r_depth + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("Height of tree is %d" %(max_depth(root)))
