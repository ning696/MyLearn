s = '2025'
# 判断类型的两个函数
print(type(s))
print(isinstance(s, str))
# str转int和float
n = int(s)
n3 = float(s)
print(n, type(n))
print(n3, type(n3))

# float转int
s1 = 123.45
n1 = int(s1)
print(n1, type(n1))

# bool转int
s2 = True
n2 = int(s2)
print(n2, type(n2))

s3 = ''
print(bool(s3), type(bool(s3)))

arr = [1, 2, 3]
arr2 = []
print(bool(arr), type(bool(arr)))
print(bool(arr2), type(bool(arr2)))

s4 = 45
print(bool(s4), type(bool(s4)))

# 查看变量的内存地址
print(id(s4))
