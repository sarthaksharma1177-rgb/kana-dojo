"""Two Sum II - Input Array Is Sorted - LeetCode Medium Problem

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

You may assume each input has exactly one solution and you cannot use the same element twice.
Return the indices of the two numbers as an integer array.

Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Indices are 1-indexed.

Approach: Two Pointers (Optimal)
- Use two pointers: left at start, right at end
- If sum equals target, return indices
- If sum is less than target, move left pointer right (need larger sum)
- If sum is greater than target, move right pointer left (need smaller sum)

Time Complexity: O(n)
Space Complexity: O(1)
"""

def twoSum(numbers, target):
    """
    Find two numbers that add up to target in sorted array.
    
    Args:
        numbers: List of sorted integers (1-indexed problem, 0-indexed list)
        target: Target sum
    
    Returns:
        List with 1-indexed positions [i, j]
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No solution found


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
    ]
    
    print("Testing Two Sum II Solution")
    print("=" * 50)
    
    for numbers, target, expected in test_cases:
        result = twoSum(numbers, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {numbers}, Target: {target}")
        print(f"Expected: {expected}, Got: {result} | {status}\n")
