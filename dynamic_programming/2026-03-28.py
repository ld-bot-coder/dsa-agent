"""
Problem: Minimum Path Sum in a Grid
Difficulty: Medium

Problem Statement:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

Example:
Input: grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
Output: 7
Explanation: The path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Approach:
This problem is solved using Dynamic Programming (DP) with a 2D DP table.
The DP table dp[i][j] represents the minimum path sum to reach cell (i, j).
The recurrence relation is:
- dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) for i > 0 and j > 0.
- For the first row and first column, the path can only come from one direction.
Time Complexity: O(m * n), where m and n are the dimensions of the grid.
Space Complexity: O(m * n), which can be optimized to O(n) by using a 1D array.
"""

def min_path_sum(grid):
    """
    Calculate the minimum path sum from the top-left to the bottom-right of a grid.

    Args:
        grid (List[List[int]]): A 2D list of non-negative integers.

    Returns:
        int: The minimum path sum.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # Initialize the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Initialize the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

if __name__ == "__main__":
    # Test cases
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert min_path_sum(grid1) == 7

    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert min_path_sum(grid2) == 12

    grid3 = [
        [1, 2],
        [1, 1]
    ]
    assert min_path_sum(grid3) == 3

    grid4 = [
        [1]
    ]
    assert min_path_sum(grid4) == 1

    print("All test cases pass")