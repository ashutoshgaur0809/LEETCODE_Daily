from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right.

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        # Step 1: Perform BFS to calculate the level sums
        level_sums = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)
        
        # Step 2: Sort the level sums in descending order
        level_sums.sort(reverse=True)
        
        # Step 3: Check if we have at least k levels
        if len(level_sums) < k:
            return -1
        
        # Step 4: Return the kth largest level sum
        return level_sums[k - 1]


# You are given the root of a binary tree and a positive integer k.

# The level sum in the tree is the sum of the values of the nodes that are on the same level.

# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

# Note that two nodes are on the same level if they have the same distance from the root.

 

# Example 1:


# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.
# Example 2:


# Input: root = [1,2,null,3], k = 1
# Output: 3
# Explanation: The largest level sum is 3.
 