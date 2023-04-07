from typing import List


class Solution(object):

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        """
        ans = 0
        for i in range(32):
            if n & 1:
                ans = ans + 2 ** (31 - i)
            n = n >> 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    coins = [1,2,5]
    amount = 11
    print(solution.coinChange(coins, amount))
