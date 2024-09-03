class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
     
        a = []
        for i,j in d.items():
            # print(j)
            a.append(j)

        b = sorted(a)

        for i in range(len(b)-1):
            for j in range(i+1,i+2):
                if b[i] == b[j]:
                    return False
        
        return True
            

        
        
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
