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
# 输入并去除前后空白
user = input('请输入用户名：').strip()
pwd = input('请输入密码：').strip()
for i in users:
    if user == i['name'] and pwd == i['pwd'] and i['status']:
        print('登录成功')
        break
    else:
        print('登录失败')
