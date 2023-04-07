
# 靜態 寫好放在上面 以文字表達 程式一運行就照著做
# 靜態的設定屬性法
class A:
    """Nothing"""

a = A()

print('==A類別的原本name屬性(靜態設定)==')
a.name = 'leia' 
print(a.name)

# 但若今天想要更改 name 屬性為 brian, 靜態方法就得在下面重設 a.name = 'brian'
print('==A類別修改後的name屬性==')
a.name = 'brian'
print(a.name)





# 動態 運作起來後 傳遞參數 根據參數運作
class B:
    """Nothing"""

b = B()

print('==B類別的原本name屬性(動態設定)==')
setattr(b, 'name', 'LEIA')
print(getattr(b, 'name'))

# 動態方法直接用 getattr 不用像靜態一樣特地去加一行
print('==B類別修改後的name屬性==')
setattr(b, 'name', 'BRIAN')
print(getattr(b, 'name'))




