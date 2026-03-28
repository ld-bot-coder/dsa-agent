"""
DP Problem 2026-03-29: Minimum Path Sum in a Grid
Difficulty: Medium

Problem Statement:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

Example:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Approach:
This problem is solved using Dynamic Programming (DP) with a 2D DP table.
The DP table dp[i][j] represents the minimum path sum to reach cell (i, j).
We initialize the first row and first column by accumulating the sums from the left and top respectively.
For other cells, dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
Time Complexity: O(m*n), Space Complexity: O(m*n) (can be optimized to O(n) if needed).
"""

def min_path_sum(grid):
    """
    Calculate the minimum path sum from top-left to bottom-right in a grid.

    Args:
        grid (List[List[int]]): A 2D grid of non-negative integers.

    Returns:
        int: The minimum path sum.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

if __name__ == "__main__":
    # Test cases
    assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert min_path_sum([[1,2,3],[4,5,6]]) == 12
    assert min_path_sum([[1]]) == 1
    assert min_path_sum([[1,2],[1,1]]) == 3
    print("All tests passed!")