class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        
        # Calculate the total sum needed for (m + n) rolls to achieve the given mean
        target_total = (m + n) * mean
        remaining_total = target_total - sum(rolls)

        # if remaining total is less than n it means that we need a value less than 1 which is not possible in Dice. hence, return empty list
        if remaining_total < n: 
            return []
        # if remaining total is greater than 6 * n it means that we need a value greater than 6 which is not possible in Dice. hence, return empty list
        if remaining_total > 6 * n:
            return []
        
        # Distribute the remainder evenly across the 'n' rolls
        base = remaining_total // n
        extra = remaining_total % n  # Extra value to distribute among some other rolls
        
        ans = [base] * n
        
        # Distribute the extra ones to the first 'extra' rolls
        for i in range(extra):
            ans[i] += 1
        
        return ans


# Example 1:

# Input: rolls = [3,2,4,3], mean = 4, n = 2
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
# Example 2:

# Input: rolls = [1,5,6], mean = 3, n = 4
# Output: [2,3,2,2]
# Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
# Example 3:

# Input: rolls = [1,2,3,4], mean = 6, n = 4
# Output: []
# Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are
