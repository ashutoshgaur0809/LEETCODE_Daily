class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        x = ""
        m = min(len(s1),len(s2))
        for i in range(m):
            x += s1[i]+s2[i]
        if len(s1) != len(s2):
            if len(s1) > len(s2):
                x += s1[m:]
            elif len(s1) < len(s2):
                x += s2[m:]

        
        return x


# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
        
