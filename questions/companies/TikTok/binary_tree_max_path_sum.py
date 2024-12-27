'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root) -> int:
    answer = root.val

    def max_sum(node):
        nonlocal answer 

        if not node:
            return 0
        
        left = max_sum(node.left)
        right = max_sum(node.right)

        max_left_right = max(left, right,0)
        sum_root_max_left_right = node.val + left + right  
        current_sum = node.val + max_left_right

        answer = max(answer, current_sum, sum_root_max_left_right)

        return current_sum
    max_sum(root)
    return answer

left = TreeNode(2)
right = TreeNode(3, TreeNode(4), TreeNode(5))
root = TreeNode(1,left,right)

print(maxPathSum(root))
