def maxArea(height):
    """Container With Most Water - LeetCode 11 (Medium)"""
    max_area = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))  # 49
