"""
Problem: Maximum Sum of Non-Adjacent Elements with Limited Selection
Difficulty: Medium

Problem Statement:
Given an array of integers, find the maximum sum of a subset of non-adjacent elements where you can select at most `k` elements.
If `k` is 0, the sum is 0. If the array is empty, the sum is 0.

Examples:
1. Input: nums = [3, 2, 5, 10, 7], k = 2
   Output: 15 (select 3 and 10 or 5 and 10)
2. Input: nums = [3, 2, 5, 10, 7], k = 3
   Output: 18 (select 3, 5, and 10)
3. Input: nums = [1, 2, 3, 4, 5], k = 1
   Output: 5 (select 5)

Approach:
This problem is solved using Dynamic Programming with a 2D DP table where:
- dp[i][j] represents the maximum sum achievable up to the i-th element with j selections.
- The recurrence relation is:
  - If we skip the i-th element: dp[i][j] = dp[i-1][j]
  - If we take the i-th element: dp[i][j] = dp[i-2][j-1] + nums[i] (if i >= 2 and j >= 1)
- Time Complexity: O(n * k), where n is the number of elements in the array.
- Space Complexity: O(n * k), optimized to O(k) by reusing rows.
"""

def max_sum_non_adjacent_with_k(nums, k):
    """
    Find the maximum sum of non-adjacent elements with at most k selections.

    Args:
        nums: List of integers.
        k: Maximum number of elements to select.

    Returns:
        Maximum sum achievable.
    """
    n = len(nums)
    if n == 0 or k == 0:
        return 0

    # Initialize DP table: dp[j] represents the maximum sum with j selections up to the current element.
    dp_prev = [0] * (k + 1)  # Represents dp[i-2][j]
    dp_current = [0] * (k + 1)  # Represents dp[i-1][j]

    for i in range(n):
        for j in range(k, 0, -1):  # Iterate backwards to avoid overwriting
            if i >= 1:
                # Option 1: Skip the current element
                skip = dp_current[j]
                # Option 2: Take the current element (if possible)
                take = 0
                if i >= 1:
                    take = dp_prev[j - 1] + nums[i]
                dp_current[j] = max(skip, take)
        # Update dp_prev for the next iteration
        dp_prev = dp_current.copy()

    return dp_current[k]

if __name__ == "__main__":
    # Test cases
    assert max_sum_non_adjacent_with_k([3, 2, 5, 10, 7], 2) == 15
    assert max_sum_non_adjacent_with_k([3, 2, 5, 10, 7], 3) == 18
    assert max_sum_non_adjacent_with_k([1, 2, 3, 4, 5], 1) == 5
    assert max_sum_non_adjacent_with_k([1, 2, 3, 4, 5], 0) == 0
    assert max_sum_non_adjacent_with_k([], 2) == 0
    assert max_sum_non_adjacent_with_k([5, 1, 2, 3, 4], 2) == 8
    print("All tests passed!")