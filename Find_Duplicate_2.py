class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        
        l = []
        for i,j in d.items():
            if j == 1:
                l.append(i)
        
        return l[:]


# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]
