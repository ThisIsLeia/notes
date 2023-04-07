"""
實體方法 Instance Method
類別方法 Class Method
靜態方法 Static Method
"""


class Cars:

    # 類別屬性
    door = 4

    # 建構式
    def __init__(self, color='blue', seat=4):
        self.color = color
        self.seat = seat

    # 實體方法(Instance Method), 要有參數 self 在方法被呼叫的時候指向物件(Object)本身
    def drive(self):
        print(f'{self} is {self.color}')
        self.message()
        # 在實體方法中可以透過self.__class__屬性(Attribute)來改變類別屬性
        self.__class__.door = 5

    # 靜態方法(Static Method)在類別(Class)中是一個獨立的方法(Method)，
    # 通常應用於方法(Method)中無需存取物件(Object)的屬性(Attribute)或方法(Method)，單純執行傳入參數或功能上運算的情況
    @staticmethod
    def message():
        print('What a beautiful car!')

    @staticmethod
    def speed(distance, minute):
        return distance / minute

    # 類別方法(Class Method)的cls參數指向類別(Class)，所以類別方法(Class Method)僅能改變類別的狀態，而無法改變物件(Object)的狀態
    @classmethod
    def open_door(cls):
        print(f'{cls} has {cls.door} doors.')

    @classmethod
    def van(cls):
        """箱型車"""
        return cls('black', 6)

    @classmethod
    def sport_car(cls):
        """跑車"""
        return cls('red', 2)


if __name__ == '__main__':
    toyota = Cars()
    # 類別屬性可以直接透過類別呼叫
    print('Cars original door: ', Cars.door)
    toyota.drive()
    print('Cars new door: ', Cars.door)

    # 透過物件呼叫類別方法
    toyota.open_door()

    # 透過類別呼叫類別方法
    Cars.open_door()

    # 透過類別方法(Class Method)可以將邏輯封裝起來，來源端只要依需求呼叫相應的類別方法(Class Method)來建立物件(Object)即可。
    # 想要跑車則呼叫跑車類別方法(Class Method)來建立跑車，至於物件(Object)的初始化過程(建造跑車的過程)封裝在類別方法中(Class Method)，
    # 它會幫我們完成並回傳，就像建立物件(Object)的工廠一樣，所以類別方法(Class Method)也被稱為工廠方法(Factory Method)
    van = Cars.van()
    sports_car = Cars.sport_car()

    # 靜態方法 可以透過物件呼叫
    print('van rate:', van.speed(1000, 20))

    # 靜態方法 可以透過類別呼叫
    print('van message:', Cars.message())

