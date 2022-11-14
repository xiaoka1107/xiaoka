# 3.列表[1,2,3,4,5,5,2,3,2,4]	去重，不能使用现有函数（10分）
def quchogn():
    list1 = [1, 2, 3, 4, 5, 5, 2, 3, 2, 4]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)


"""4.比如有这样一个文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
----------------------------
lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19
----------------------------
请通过代码读取文件并输出年龄大于18岁的人名"""


def writename():
    str1 = "lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19"
    list1 = str1.split(",")
    data = open("data.txt", "w", encoding="utf-8")
    for i in list1:
        data.write(i + "\n")
    data.close()


def findname():
    data = open("data.txt", "r", encoding="utf-8")  # 读取文件
    list1 = []
    n = len(data.readlines())  # 获取文件行
    data.seek(0)  # 指针归0
    for i in range(n):  # 遍历文件
        ss = data.readline()
        key, value = ss.split(":")
        value = int(value)
        if value >= 18:  # 判断
            list1.append(key)
    return list1


def tuidao():
    list1 = []
    for i in range(1, 101):
        if i % 3 == 0:
            list1.append(i)
    return list1


"""
7.有一堆字符串，“welocme to super&Test”，打印出emcolew ot  
tseT&repus……全部单词原位置反转，不能使用索引倒序输出或者通过其
他现有函数实现，自己写字符串首尾交换方法（15分）
"""


def aaa():
    str1 = "welocme to super&Test"
    list1 = str1.split(" ")
    list2 = []
    for i in list1:
        i = list(i)
        n = len(i) // 2
        for j in range(n):
            i[j], i[(len(i) - 1 - j)] = i[(len(i) - 1 - j)], i[j]
        # i = str(i)
        list2.append(i)
    # print(list2)
    for i in range(len(list2)):
        c = "".join(list2[i])
        print(c, end=" ")
    return c


# 斐波那契数

def feibo(n=100):
    list1 = [1, 1]
    for i in range(2, n):
        list1.append(list1[i-1] + list1[i-2])
    return list1



if __name__ == '__main__':
    aa = findname()
    print(aa)
    print(findname())
    print(tuidao())
    print(feibo(100))