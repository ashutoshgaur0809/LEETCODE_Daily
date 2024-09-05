class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Initialize pointers for s and t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # Check if current characters match
                i += 1  # Move pointer in s
            j += 1  # Always move pointer in t
        
        # Check if all characters in s were found in t
        return i == len(s)

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
