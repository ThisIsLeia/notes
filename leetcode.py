from typing import List

class LeetcodeService:
    
    @classmethod
    def get_service_names(cls):
        """ 取得可以使用的 services """
        print('== 當前可以選用的 services ==')
        for klass in cls.__subclasses__():
            print(klass.__name__.lower())


    @classmethod
    def get_service(cls, name, **kwargs):
        for klass in cls.__subclasses__():
            name = name.lower()
            if klass.__name__.lower() == name:
                print(f'== find the service [{name}] ==')
                return klass(**kwargs)
        raise NotImplementedError('請確認輸入名稱是否正確')
    
    @classmethod
    def service_menager(cls, name, **kwargs):
        return cls.get_service(name, **kwargs)

class DP(LeetcodeService):
    """
    Dynamic Programing
    """

    NAME = 'dp'
    HIDDEN = ['name', '__module__', '__doc__', 'NAME', '__init__', 'get_service_names', 'get_service', 'service_menager', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', 'HIDDEN', 'get_assignments', 'hidden', 'assignments_manager']

    def __init__(self, name=NAME, hidden=HIDDEN):
        self.name = name
        self.hidden = hidden

    def get_assignments(self):
        assignments = [assignment for assignment in dir(self) if assignment not in self.hidden]
        for assignment in assignments:
            print(assignment)

    def assignments_manager(self, assignment_name):
        assignment = self.__class__.__dict__.get(assignment_name)
        if assignment:
            return assignment()
    
    def coin():
        """
        Dynamic Programing - Coin Change
        """
        # Dynamic Programing (當發現必須要用兩個迴圈解題時)

        coins = list(map(lambda x: int(x), (input('請輸入 coins: ')).split(",")))
        amount = int(input('請輸入 amount: '))

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
    
    def aaa(self):
        ...
    


class Graph(LeetcodeService):
    ...
                

dp = DP()

if __name__ == '__main__':
    LeetcodeService.get_service_names()

    topic = input('請輸入欲選用主題：')
    service = LeetcodeService.service_menager(topic)

    print(f'== {topic} 可以選用的 assignments ==')
    service.get_assignments()

    assignment = input('請輸入欲選用assignment: ')
    service.assignments_manager(assignment)
