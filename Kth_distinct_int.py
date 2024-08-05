class Solution:
    def kthDistinct(self, s: List[str], k: int) -> str:
        d = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        l = []
        for i,j in d.items():
            if j == 1:
             l.append(i)

        if len(l) == k:
            return l[k-1]

        if len(l) < k:
            return ""

        return l[k-1]

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 
# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
        
