class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        # Step 1: Check if s1 + s2 is equal to s2 + s1
        if s1 + s2 != s2 + s1:
            return ""
        
        # Step 2: Find the GCD of the lengths of s1 and s2
        gcd_length = gcd(len(s1), len(s2))
        
        # Step 3: Return the substring of s1 that represents the GCD string
        return s1[:gcd_length]

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
