```python
"""
Problem: Maximum Sum of Non-Adjacent Elements in a Circular Array
Difficulty: Medium

Problem Statement:
Given a circular array of integers, find the maximum sum of non-adjacent elements.
In a circular array, the first and last elements are considered adjacent.
You cannot select adjacent elements, and the array is circular, so the first and last elements cannot be selected together.

Examples:
1. Input: [2, 3, 2]
   Output: 3
   Explanation: You can select 3 (index 1), but not 2 (index 0) and 2 (index 2) together.

2. Input: [5, 1, 2, 4]
   Output: 8
   Explanation: You can select 5 (index 0) and 4 (index 3), but not 1 (index 1) and 2 (index 2) together.

Approach:
This problem is solved using dynamic programming. The circular nature of the array means we cannot directly apply the standard non-adjacent sum DP approach.
Instead, we break the problem into two cases:
1. Exclude the first element and solve the problem for the remaining linear array.
2. Exclude the last element and solve the problem for the remaining linear array.
The solution is the maximum of these two cases.

The standard non-adjacent sum problem is solved using DP where:
- dp[i] represents the maximum sum up to index i.
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])

Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(1), as we only use a few variables to store intermediate results.
"""

def max_circular_non_adjacent_sum(nums):
    """
    Calculate the maximum sum of non-adjacent elements in a circular array.

    Args:
        nums: List of integers representing the circular array.

    Returns:
        Maximum sum of non-adjacent elements.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def linear_non_adjacent_sum(arr):
        prev_prev = 0
        prev = arr[0]
        for i in range(1, len(arr)):
            current = max(prev, prev_prev + arr[i])
            prev_prev, prev = prev, current
        return prev

    # Case 1: Exclude the first element
    case1 = linear_non_adjacent_sum(nums[1:])
    # Case 2: Exclude the last element
    case2 = linear_non_adjacent_sum(nums[:-1])

    return max(case1, case2)

if __name__ == "__main__":
    # Test cases
    assert max_circular_non_adjacent_sum([2, 3, 2]) == 3
    assert max_circular_non_adjacent_sum([5, 1, 2, 4]) == 8
    assert max_circular_non_adjacent_sum([1, 2, 3, 4, 5]) == 9
    assert max_circular_non_adjacent_sum([1, 2, 3, 4, 5, 6]) == 12
    assert max_circular_non_adjacent_sum([1]) == 1
    assert max_circular_non_adjacent_sum([1, 2]) == 2
    assert max_circular_non_adjacent_sum([1, 2, 3]) == 3
    assert max_circular_non_adjacent_sum([1, 2, 3, 4]) == 6
    assert max_circular_non_adjacent_sum([1, 2, 3, 4, 5, 6, 7]) == 16
    print("All test cases passed!")
```