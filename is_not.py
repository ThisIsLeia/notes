class A:
    pass


a = A()

b = a

print(a)
print(b)

print(a is b)  # ==> 判斷兩個變數之間的『記憶體位址』是否相同
print(a == b)  # ==> 判斷兩個變數之間的『值』是否相同


