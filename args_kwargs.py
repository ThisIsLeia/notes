def test(required, *args, **kwargs):
    """
    * 收集的引數會被放到一個 tuple 中
    ** 會把鍵值對做成字典
    """
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


def sum_(*args):
    """ * 收集的引數會被放到一個 tuple 中"""
    result = 0
    for i in args:
        result += i
    return print(result)


def make_dict(**kwargs):
    """把傳進來的 XXX=XXX 做成字典"""
    print(kwargs)


if __name__ == '__main__':
    print('打包==>')
    test(1, 2, 3, 4, name='Leia', number=27)

    print('\n透過迭代將打包的東西加總==>')
    sum_(1, 2, 3, 4, 5)

    print('\n** 拆解字典==>')
    print(
        " 常用把在接口傳進來的字典，變成 XXX=XXX 作為搜尋條件\n",
        "filters = {'user_name': 'Leia', 'user_id': 47}\n",
        "db.session.query(Account).filter_by(**filters)\n",
        ""
        )

    print('\n** 製作字典==>')
    print(" 把傳進來的 XXX=XXX 做成字典")
    make_dict(phone='0988495143', status=True)

    print('====== 前面有**的東西就是 XXX=XXX ======')


