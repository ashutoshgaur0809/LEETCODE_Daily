class Solution:
    def countSeniors(self, s) -> int:
        clk = 0
        for i in s:
                if int(i[11:13]) > 60:
                    clk += 1
        
        return clk


# Example 1:

# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
# Example 2:

# Input: details = ["1313579440F2036","2921522980M5644"]
# Output: 0
# Explanation: None of the passengers are older than 60.