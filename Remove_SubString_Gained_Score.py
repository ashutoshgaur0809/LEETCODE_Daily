class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            # First prioritize removing "ba"
            first = "ba"
            second = "ab"
            first_points = y
            second_points = x
        else:
            # First prioritize removing "ab"
            first = "ab"
            second = "ba"
            first_points = x
            second_points = y
        
        # Function to calculate points by removing a particular substring
        def calculate_points(substring, points):
            nonlocal s
            p = 0
            i = 0
            while i < len(s):
                if s[i:i+2] == substring:
                    # Found substring, remove it and add points
                    s = s[:i] + s[i+2:]
                    p += points
                    # Rewind i to check for adjacent substrings
                    i = max(0, i - 1)
                else:
                    i += 1
            return p
        
        # Repeat the process until no more substrings can be removed
        total_points = 0
        while True:
            points1 = calculate_points(first, first_points)
            points2 = calculate_points(second, second_points)
            
            # If no more substrings can be removed, break the loop
            if points1 == 0 and points2 == 0:
                break
            
            # Accumulate the points
            total_points += points1 + points2
        
        return total_points

# Example usage:
sol = Solution()
print(sol.maximumGain("cdbcbbaaabab", 4, 5))  # Output: 19
print(sol.maximumGain("aabbaaxybbaabb", 5, 4))  # Output: 20
