"""
3、摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""


# 定义类(家具
class Furniture:
    # 初始化
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name}: 占{self.area}平米"


# 定义房子类
class House:
    # 初始化
    def __init__(self, name, htype="南北", areas=100, areaz=120, *args):
        self.area_z = areaz  # 总面积
        self.name = name  # 名
        self.hType = htype  # 户型
        self.s_area = areas  # 剩余面积
        self.furnitures = []  # 家具


    # 放家具
    def addfurnit(self, furniture):
        # 判断家具是否能放进去
        if furniture.area < self.s_area:
            self.furnitures.append(furniture.name)
            self.s_area -= furniture.area
            print(f"{self.name}放了家具{furniture.name}")
        else:
            print(f"放不下{furniture.name},退回")

    # 返回房子状态
    def __str__(self):
        return f"房子名:{self.name},户型:{self.hType},总面积:{self.area_z},剩余面积:{self.s_area},摆放家具有:{self.furnitures}"


if __name__ == '__main__':
    # 定义家具
    bed = Furniture("bed", 4)
    # print(bed)
    wardrobe = Furniture("wardrobe", 2)
    table = Furniture("table", 1.5)

    # 实例化房子
    house1 = House("house1", "东西3居室", 100)
    house2 = House("house2", "北向开间", 10, 20)
    house1.addfurnit(bed)
    print(house1)
    house1.addfurnit(wardrobe)
    house1.addfurnit(table)
    house1.addfurnit(bed)
    print(house1)
    house2.addfurnit(bed)
    house2.addfurnit(wardrobe)
    house2.addfurnit(bed)
    house2.addfurnit(table)
    print(house2)

