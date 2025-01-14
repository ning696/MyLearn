try:
    num = 1 / 0
except Exception as e:
    print(e)
finally:
    print('执行finally')
raise Exception('出现错误')