import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        roots = []
        roots.append(root)
        while len(roots) > 0:
            cur_root = roots.pop(0)
            print(cur_root.data, end=' ')
            if cur_root.left is not None:
                roots.append(cur_root.left)
            if cur_root.right is not None:
                roots.append(cur_root.right)
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
