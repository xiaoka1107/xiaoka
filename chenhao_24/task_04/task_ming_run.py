"""2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤
"""


# 定义类
class Person:
    # 属性
    def __init__(self, name, weith):
        self.name = name
        self.weith = weith

    def run(self, n=1):
        self.weith -= 0.5 * n
        print(f"{self.name}跑了{n}圈,体重减了{0.5 * n}kg")

    def eat(self, n=1):
        self.weith += n
        print(f"{self.name}吃了{n}kg,体重加了1kg")

    def __str__(self):
        return f"{self.name}现在的体重是{self.weith}"


if __name__ == '__main__':
    xiaoming = Person("xiaoming", 75)
    xiaomei = Person("xiaomei", 45)
    print(xiaomei, xiaoming)
    xiaoming.run(4)
    xiaomei.eat()
    print(xiaomei)
    xiaomei.run(10)
    xiaoming.run(20)
    print(xiaomei, xiaoming)
    xiaoming.eat(20)
    print(xiaomei, xiaoming)
