"""
烤地瓜

"""


# 定义地瓜类
class SweetPotato():
    # 定义初始属性
    def __init__(self, name):
        # 被考时间
        self.ctime = 0
        # 地瓜初始状态
        self.status = "生的"
        self.name = name
        self.condiments = []  # 调料

    # 烤地瓜方法
    def cookSP(self, t):
        # 焙烤时间t

        if t < 0:
            print("无效参数")
            return "非法"
        self.ctime += t
        # 状态
        if 0 <= self.ctime <= 3:
            self.status = "生的"
            # print(f"考了{self.ctime}min,地瓜状态是: {self.status}")
        elif 3 < self.ctime < 5:
            self.status = "半生的"
            # print(f"考了{self.ctime}min,地瓜状态是: {self.status}")
        elif 5 <= self.ctime <= 8:
            self.status = "熟的"
            # print(f"考了{self.ctime}min,地瓜状态是: {self.status}")
        else:
            self.status = "烤糊了"
            # print(f"考了{self.ctime}min,地瓜状态是: {self.status}")

    # 撒调料方法
    def condiment(self, *args):
        self.condiments.extend(*args)
        print(f"{self.name}撒了{self.condiments}调料")

    def __str__(self):
        # 返回地瓜状态信息
        return f"{self.name}考的时间是{self.ctime},状态是{self.status},撒了{self.condiments}调料"


if __name__ == '__main__':
    sweetpotato1 = SweetPotato("地瓜1")
    print(sweetpotato1)
    sweetpotato2 = SweetPotato("地瓜2")
    sweetpotato1.cookSP(1)
    sweetpotato1.condiment(("salt", "sugar"))
    print(sweetpotato1)
    sweetpotato2.cookSP(3)
    sweetpotato1.cookSP(2)
    sweetpotato1.cookSP(4)
    sweetpotato2.cookSP(6)
    print(sweetpotato1)
    print(sweetpotato2)
    sweetpotato1.cookSP(-2)
    print(sweetpotato1)
