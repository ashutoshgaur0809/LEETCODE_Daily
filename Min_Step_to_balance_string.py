class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0
        total_b = s.count('b')
        total_a = s.count('a')
        
        if total_a == 0:
            # If there are no 'a's, the string is already balanced
            return 0
        if total_b == 0:
            # If there are no 'b's, the string is already balanced
            return 0
        
        b_count = 0  # Number of 'b's encountered so far
        a_count = 0  # Number of 'a's encountered so far
        min_deletions = float('inf')  # Initialize to a large number

        # First pass to count total number of 'a's
        total_a = s.count('a')

        # Traverse the string and calculate deletions needed
        for char in s:
            if char == 'b':
                b_count += 1
            elif char == 'a':
                a_count += 1
                # Calculate deletions needed if we want to make the string balanced up to this point
                deletions_needed = b_count + (total_a - a_count)
                min_deletions = min(min_deletions, deletions_needed)

        # Check if we need to remove all 'b's (if there are no 'a's at all)
        min_deletions = min(min_deletions, b_count)

        return min_deletions
           
