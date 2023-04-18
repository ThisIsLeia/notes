from typing import List


class Solution(object):

    def coin(self, coins, amount):
        # Dynamic Programing (當發現必須要用兩個迴圈解題時)
        
        # 第一步：初始化數據
        # dp 数组初始化为 amount+1，因为总金额最多需要 amount 枚硬币
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # 金额为 0 时不需要任何硬币
        print('dp ===>', dp)
        print('================================')
        
        for i in range(1, amount + 1):
            for coin in coins:
                print('current i: ', i, '\tcurrent coin: ', coin)
                # i 需要大於等於 coin 才能繼續，因為需要已知的 i 才能計算
                if i >= coin:
                    print('dp[i] ->', dp[i], '\tdp[i - coin] + 1 ->', dp[i - coin] + 1)
                    # dp[i] 會記下 min(最多幣數的情況之所需幣數, (最多幣數的情況-當前面額)之面額所需幣數 +1)
                    # (最多幣數的情況-當前面額)+1 ==> 意即 算入當前幣額後的總幣數
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    print('current dp ===>', dp)
                    print('--------------------------------')
        print('final', dp[amount])
        return -1 if dp[amount] == amount + 1 else dp[amount]
                

solution = Solution()

if __name__ == '__main__':
    # Dynamic Programing - Coin Change
    coins = [1,2,5]
    amount = 11
    print(solution.coin(coins, amount))
