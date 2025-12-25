# Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    """
    226. Invert Binary Tree
    Given the root of a binary tree, invert the tree, and return its root.
    """
    pass

def max_depth(root):
    """
    104. Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.
    """
    pass

def diameter_of_binary_tree(root):
    """
    543. Diameter of Binary Tree
    Given the root of a binary tree, return the length of the diameter of the tree.
    """
    pass

def is_balanced(root):
    """
    110. Balanced Binary Tree
    Given a binary tree, determine if it is height-balanced.
    """
    pass

def is_same_tree(p, q):
    """
    100. Same Tree
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    """
    pass

def is_subtree(root, subRoot):
    """
    572. Subtree of Another Tree
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root 
    with the same structure and node values of subRoot and false otherwise.
    """
    pass

def lowest_common_ancestor(root, p, q):
    """
    235. Lowest Common Ancestor of a Binary Search Tree
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    """
    pass

def level_order(root):
    """
    102. Binary Tree Level Order Traversal
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    """
    pass

def right_side_view(root):
    """
    199. Binary Tree Right Side View
    Given the root of a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.
    """
    pass

def good_nodes(root):
    """
    1448. Count Good Nodes in Binary Tree
    Given a binary tree root, a node X in the tree is named good if in the path from root to X 
    there are no nodes with a value greater than X.
    """
    pass

def is_valid_bst(root):
    """
    98. Validate Binary Search Tree
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    """
    pass

def kth_smallest(root, k):
    """
    230. Kth Smallest Element in a BST
    Given the root of a binary search tree, and an integer k, return the kth smallest value 
    (1-indexed) of all the values of the nodes in the tree.
    """
    pass

def build_tree(preorder, inorder):
    """
    105. Construct Binary Tree from Preorder and Inorder Traversal
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
    and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    """
    pass

def max_path_sum(root):
    """
    124. Binary Tree Maximum Path Sum
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
    has an edge connecting them. Return the maximum path sum of any non-empty path.
    """
    pass

class Codec:
    """
    297. Serialize and Deserialize Binary Tree
    Design an algorithm to serialize and deserialize a binary tree.
    """
    def serialize(self, root):
        pass
        
    def deserialize(self, data):
        pass
