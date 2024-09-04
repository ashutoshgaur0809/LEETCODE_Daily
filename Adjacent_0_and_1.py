from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Edge case: If no flowers need to be planted, we can always return True.
        if n == 0:
            return True
        
        # Iterate through the flowerbed
        for i in range(len(flowerbed)):
            # Check if the current spot is empty
            if flowerbed[i] == 0:
                # Check if the left neighbor is empty or it's the boundary
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right neighbor is empty or it's the boundary
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both neighbors are empty (or we're at the boundaries), plant a flower
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant a flower here
                    n -= 1  # Decrease the number of flowers to plant
                    
                    # If all flowers have been planted, return True
                    if n == 0:
                        return True
        
        # If we finished the loop and still have flowers left to plant, return False
        return False

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
