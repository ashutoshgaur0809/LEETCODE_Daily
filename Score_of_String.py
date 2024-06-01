class Solution:
    def scoreOfString(self, s: str) -> int:
        l = []
        for i in s:
            l.append(ord(i))
        
        sum = 0
        for i in range(len(l)-1):
            sum += abs(l[i] - l[i+1])
        
        return sum


# Input: s = "hello"

# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: s = "zaz"

# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.