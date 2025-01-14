date = input('输入日期').split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])
num = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (not year % 4 and year % 100) or not year % 400:
    num[2] += 1
result = 0
for i in range(month):
    result += num[i]
result += day
print(result)
