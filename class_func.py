class Base:
    def one(self):
        raise NotImplementedError

    def two(self):
        raise NotImplementedError


class Child(Base):
    def one(self):
        self.two()
        print('第一步實作')

    def two(self):
        print('第二步實作')

    def test(self):
        if self.__class__.__dict__.get("one"):
            print("拿到one!")
            return self.__class__.one


if __name__ == '__main__':
    print('Base', Base.__dict__)
    print('Child', Child.__dict__)
    c = Child()
    c.test()



'''
__class__ 會呼叫自身類別
__dict__ 會呼叫該類別所有的實作
'''

