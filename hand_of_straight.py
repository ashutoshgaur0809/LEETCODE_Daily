# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

# hand = [8,10,12] groupsize = 3
# output = False
# Explain - diff bw each value is never greater than one
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        hand = sorted(hand)
        if len(hand)%groupSize == 0:
            for i in range(len(hand)-2,-1,-1):
                if abs(hand[i] - hand[i+1]) > 1:
                    print(False)

            print(True)
        else:
            print(False)
    
s = Solution()
print(s.isNStraightHand([1,2,3,4,5,6,7,8,9],3))
        