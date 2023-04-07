class A:
    def __init__(self, name, number):
        self.name = name
        self.number = number


leia = A('Leia', 47)
print(leia)
# 出來會是 <__main__.A object at 0x7fac780a5588>


class B:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f'name={self.name}, number={self.number}'


brian = B('Brian', 11)
print(brian)
# 透過 __repr__ 可以自己定義要印的結果
