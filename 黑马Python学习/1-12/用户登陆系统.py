users = [{
    'name': '小红',
    'pwd': '123',
    'status': True
}, {
    'name': '小明',
    'pwd': '456',
    'status': False
}, {
    'name': 'jack',
    'pwd': '789',
    'status': True
}]
print(users)
flag = False
# 输入并去除前后空白
for i in range(3):
    user = input('请输入用户名：').strip()
    pwd = input('请输入密码：').strip()
    for j in users:
        if user == j['name']:
            if pwd == j['pwd']:
                if j['status']:
                    print('登录成功')
                    flag = True
                    break
                else:
                    print('账号被冻结')
            else:
                print('密码错误')
            break
    else:
        print('用户名称不存在')
    if flag:
        break
else:
    print('三次密码均输入错误')
