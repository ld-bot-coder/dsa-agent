```python
"""
Problem: Coin Change (Unlimited Supply)
Difficulty: Medium
Problem Statement:
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 5 + 5 + 1 = 11.

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Approach:
This problem is solved using Dynamic Programming (DP) with a bottom-up approach. The idea is to build a DP array where `dp[i]` represents the minimum number of coins needed to make the amount `i`. Initialize the DP array with a value larger than the maximum possible (e.g., `amount + 1`) to signify that the amount is initially unreachable. The base case is `dp[0] = 0` because zero coins are needed to make amount 0.

For each coin, iterate through all amounts from the coin's value up to the target amount. For each amount `i`, update `dp[i]` to be the minimum of its current value or `dp[i - coin] + 1`.

Time Complexity: O(amount * n), where n is the number of coins.
Space Complexity: O(amount), for the DP array.
"""

def coinChange(coins, amount):
    """
    Calculate the fewest number of coins needed to make up the given amount.

    Args:
        coins (List[int]): List of coin denominations.
        amount (int): Target amount to achieve.

    Returns:
        int: Minimum number of coins needed, or -1 if not possible.
    """
    # Initialize DP array with a value larger than the maximum possible (amount + 1)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    # Test cases
    assert coinChange([1, 2, 5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0
    assert coinChange([1, 3, 4], 6) == 2
    assert coinChange([2, 5, 10, 1], 27) == 4
    print("All test cases pass")
```