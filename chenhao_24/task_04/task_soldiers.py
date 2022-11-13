"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
"""


# 定义枪
class Guns:
    def __init__(self, name, bullet):
        self.name = name
        self.bullets = bullet

    # 发射
    def shoot(self, n):
        if self.bullets >= n:
            self.bullets -= n
            print(f"{self.name}开了{n}枪,剩余{self.bullets}发子弹")
        else:
            print("子弹不够,请补充弹夹")
            return False

    def addbull(self, n):
        self.bullets += n
        print(f"{self.name}增加了{n}发子弹")

    # 打印枪支状态
    def pshoot(self):
        print(f"{self.name}有{self.bullets}发子弹")

    def __str__(self):
        return f"{self.name}有{self.bullets}发子弹"


# 定义士兵
class Soldiers:
    # 初始化
    def __init__(self, name):
        self.name = name
        self.sguns = []  # 士兵的武器库

    # 给士兵配枪
    def addgun(self, gun):
        self.sguns.append(gun.name)
        print(f"{self.name}配置{gun.name}")

    # 开枪功能
    def shoot_s(self, gun, n):  # 士兵开枪
        a = gun.shoot(n)
        if a:
            print(f"士兵{self.name},使用{gun.name}开了{n}枪")

    # 换弹夹
    def addbull(self, gun, n):
        gun.addbull(n)

    def __str__(self):
        return f"{self.name}有{self.sguns}"


if __name__ == '__main__':
    AK47 = Guns("AK47", 100)
    M16A4 = Guns("M16A4", 200)
    xusanduo = Soldiers("xusanduo")
    hechenguang = Soldiers("hechenguang")
    xusanduo.addgun(M16A4)
    hechenguang.addgun(AK47)
    xusanduo.shoot_s(AK47, 50)
    hechenguang.shoot_s(M16A4, 100)
    print(AK47, M16A4, xusanduo, hechenguang)
    print("----")
    xusanduo.shoot_s(AK47, 100)
    print(AK47, M16A4, xusanduo, hechenguang)
    xusanduo.addbull(AK47,200)
    xusanduo.shoot_s(AK47, 100)
    print(AK47, M16A4, xusanduo, hechenguang)


