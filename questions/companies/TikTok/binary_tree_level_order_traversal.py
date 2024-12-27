import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root) -> list[list[int]]:
    queue = collections.deque()
    queue.append(root)
    answer = []
    
    if not root:
        return []

    while queue:
        level_array = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                level_array.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
        answer.append(level_array) 
        
    print(answer)
    return answer

levelOrder(TreeNode(1))
