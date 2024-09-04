
# Two Pointer 
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
            
        return ''.join(s)

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

# Imp Case
# s = "race car"
# output = "race car"


