"""3Sum - LeetCode Problem 15 (Medium)

Find all unique triplets that sum to 0.
Return unique triplets without duplicates.

Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Approach:
1. Sort the array
2. For each element, use two-pointer technique on remaining array
3. Skip duplicate values
4. Time: O(n^2), Space: O(1)
"""

def threeSum(nums):
    """Find all unique triplets that sum to 0."""
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if nums[i] > 0:  # No triplet possible with all positive
            break
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue
        
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]
    
    for nums, expected in test_cases:
        result = threeSum(nums.copy())
        status = "PASS" if sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected]) else "FAIL"
        print(f"{nums}: {status}")
