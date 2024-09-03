class Solution:
    def getLucky(self, s: str, k: int) -> int:

                a = ""
                sumi = 0
                l = []
                for i in s:
                    a += str((ord(i) + 4)%100)



                for i in a:
                        l.append(int(i))
                        sumi += int(i)
                    

                    
                # sumi = sum()
                ans = 0
                if k > 1:
                    
                    for i in range(1,k):
                        res = 0
                        for i in str(sumi):
                            # a += str((ord(i) + 4)%100)
                            res += int(i)
                            sumi = res
                else:
                    sumi = sumi

                return sumi

# Example 1:

# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.
# Example 2:

# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.
# Example 3:

# Input: s = "zbax", k = 2
# Output: 8
 
