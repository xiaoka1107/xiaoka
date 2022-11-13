"""
打印小猫吃鱼,小猫喝水

"""


# 定义小猫类
class Cats():
    # 小猫初始化
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.food = "fish"
        self.drink = "water"

    def eat(self):
        print(f"{self.color}的{self.name}吃{self.food}")

    def drinking(self):
        print("{self.color}的{self.name}喝{self.drink}")

    def __str__(self):
        return f"{self.color}的{self.name}吃{self.food}喝{self.drink}"


if __name__ == '__main__':
    cat1 = Cats("TOm", "blue")
    cat2 = Cats("TOni", "red")
    cat1.eat()
    cat2.drinking()
    cat1.eat()
    print(cat2, cat1)
