# 生成斐波那契数列的前20个数

a = 1
b = 1

for i in range(20):
    print(a)
    print(b)
    a = a + b
    b = a + b
