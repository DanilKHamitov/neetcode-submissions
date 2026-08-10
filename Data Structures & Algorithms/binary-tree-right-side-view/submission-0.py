# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        self.L = []
        if  root:
            q.append(root)
            self.L.append(root.val)

        while q:
            ul = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    ul.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    ul.append(node.right.val)
            if len(ul) >=1:
                self.L.append(ul[len(ul)-1])
        return self.L
        