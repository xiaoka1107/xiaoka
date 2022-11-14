"""
13、开发一个注册系统，界面可以用print打印，
保存用户名和密码，存在的用户提示已注册，不存
在的可以注册成功（提示建议使用函数划分不同的
功能，比如查询用户，新增用户）（10分）
"""
yonghu = dict()
ss = open("yonghu.txt", "r", encoding="utf-8")
n = len(ss.readlines())
ss.seek(0)
for i in range(n):
    line = ss.readline()
    line.strip()
    # print(line,end="")
    list1 = line.split(":")
    line = list(line)
    # print(list1)
    yonghu[list1[0]] = list1[1]
ss.close()
print(yonghu)


def zhuce():
    ss = open("yonghu.txt", "a", encoding="utf-8")
    name = input("请输入用户名")
    if name in yonghu:
        print("用户已存在")
    else:
        pw = input("请输入密码")
        yonghu[name] = pw
        ss.writelines(name + ":" + pw+"\n")
        print(f"注册用户{name},成功")
        ss.close()


def select():
    name = input("请输入用户名")
    if name in yonghu:
        print(f"用户{name}存在")
    elif name not in yonghu:
        print(f"{name}不存在")


if __name__ == '__main__':
    while True:
        print("\n \n 注册系统")
        a = input("注册请输入1,查询请输入2\n")
        if a == "1":
            print("开始注册用户")
            zhuce()
        elif a == "2":
            print("开始查询账户")
            select()
        else:
            print("输入有误,请重新输入")
