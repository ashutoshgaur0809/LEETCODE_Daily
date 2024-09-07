class Solution:
    def isSubPath(self, head, root):
        def checkPath(head, root):
            if not head: return True
            if not root or head.val != root.val: return False
            return checkPath(head.next, root.left) or checkPath(head.next, root.right)

        if not root: return False
        if checkPath(head, root): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



# Example 1:



# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.  
# Example 2:



# Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Example 3:

# Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

# Constraints:

# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary tree.
