def largest_altitude(gain):
    altitudes = [0]  # Start at altitude 0
    current_altitude = 0  # Initialize current altitude
    
    # Calculate all altitudes based on gain
    for g in gain:
        current_altitude += g  # Update current altitude
        altitudes.append(current_altitude)  # Store the current altitude
    
    return max(altitudes)  # Return the highest altitude

# Example 1
gain1 = [-5, 1, 5, 0, -7]
print(largest_altitude(gain1))  # Output: 1

# Example 2
gain2 = [-4, -3, -2, -1, 4, 3, 2]
print(largest_altitude(gain2))  # Output: 0
