"""
Longest Substring Without Repeating Characters - Medium Level LeetCode Problem

Problem: Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Approach: Sliding Window with Hash Map
- Use a sliding window approach with two pointers (left and right)
- Use a dictionary to track the most recent index of each character
- When we encounter a repeating character, move the left pointer to skip the previous occurrence
- Track the maximum length seen

Time Complexity: O(n) - single pass through the string
Space Complexity: O(min(m, n)) - where m is the alphabet size
"""

def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
    
    Returns:
        Length of the longest substring without repeating characters
    """
    # Dictionary to store the most recent index of each character
    char_index = {}
    max_length = 0
    left = 0  # Left pointer of the sliding window
    
    for right in range(len(s)):
        # If character is already in the current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left pointer to skip the previous occurrence
            left = char_index[s[right]] + 1
        
        # Update the most recent index of the current character
        char_index[s[right]] = right
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),       # "abc"
        ("bbbbb", 1),          # "b"
        ("pwwkew", 3),         # "wke"
        ("au", 2),             # "au"
        ("dvdf", 3),           # "vdf"
        ("", 0),               # empty string
        ("a", 1),              # single character
    ]
    
    print("Testing Longest Substring Without Repeating Characters")
    print("=" * 55)
    
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s:15}' | Expected: {expected} | Got: {result} | {status}")
