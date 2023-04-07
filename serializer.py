class Serializer:
    # 不要序列化的名單
    __hidden__ = []

    def to_json(self):
        json_data = {}
        for attr_name in self.__dir__():  # -> __dir__() 列出可以調用的屬性和方法名
            # 如果不是 ＿＿ 開頭 且 不在hidden名單內
            if not attr_name.startswith('__') and attr_name not in self.__hidden__:
                # 取得實例屬性
                attr = getattr(self, attr_name)
                # 若無法呼叫 就加進名單
                if not callable(attr):
                    json_data[attr_name] = attr
        return json_data


class A(Serializer):
    def __init__(self):
        self.name = 'leia'
        self.number = 111
        self.school = 'NSYSU'


if __name__ == '__main__':
    a = A()
    data = a.to_json()
    print(data)

# 會把 屬性名稱attr_name 和 屬性attr，編成字典
# 之後呼叫 key(屬性名稱) 就能回傳已經實例化的 value(屬性attr)
