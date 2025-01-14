users = {"小红": {
    'name': '小红',
    'pwd': '123',
    'status': True
}, "小明": {
    'name': '小明',
    'pwd': '456',
    'status': False
}, "jack": {
    'name': 'jack',
    'pwd': '789',
    'status': True
}}
print(users)
flag = False
# 输入并去除前后空白
for i in range(3):
    name = input('请输入用户名：').strip()
    pwd = input('请输入密码：').strip()
    if name in users and pwd == users[name]['pwd'] and users[name]['status']:
        print('登陆成功')
        break
    elif name in users and pwd == users[name]['pwd'] and users[name]['status'] == False:
        print('账号被封')
    elif name in users and pwd != users[name]['pwd']:
        print('密码错误')
    else:
        print('不存在该用户名')
else:
    print('超过三次')
