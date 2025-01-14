"""
字典学习
"""
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person.keys())
print(person.values())
print(person.items())
for value in person.values():
    print(value)

'''
数组学习
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 外层循环遍历矩阵的行
for row in matrix:
    # 内层循环遍历矩阵的列
    for element in row:
        print(element, end=' ')  # 输出元素，并使用空格分隔
    print()  # 输出完一行后换行

for key, value in person.items():
    print(f"{key}: {value}")

"""
for循环的else 语句:
Python中的for 循环可以带有一个else 语句块。else 中的代码在for循环正常结束时执行
(即没有通过break 跳出循环)。
"""
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished without break.")

'''
if else学习
'''
age1 = 25
has_permission = False

if not has_permission:
    print("You do not have permission.")
else:
    print("You have permission.")

age2 = 20

if age2 < 13:
    print("You are a child.")
elif age2 < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
'''
elif 用于判断多个条件，允许你在多个条件中做选择。
可以结合逻辑运算符（and、or、not）来进行复杂的条件判断。
'''


