# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        self.L = []
        self.uL =[]
        if root:
            q.append(root)
            self.uL.append(root.val)
            self.L.append(self.uL)
        
        while q:
            self.uL = []
            for i in range(len(q)):
               
                node = q.popleft()
                if node.left:
                    self.uL.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    self.uL.append(node.right.val)
            if len(self.uL) >=1:
                self.L.append(self.uL)
        return self.L    


        