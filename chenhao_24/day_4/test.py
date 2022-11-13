import my_module
# from my_module import testA

# 包别名
import my_module as mode

# from my_module_1 import testB as ttsB

from my_module import *

import sys


# from my_module_1 import my_module1
# from my_module_1 import *
import my_module_1.my_module2
import my_module_1.my_module2
if __name__ == '__main__':
    # my_module.testA(3, 1)
    # testA(3, 1)
    # mode.testB(3, 1)
    # print(testD(3, 3))
    # print(sys.path)
    # print(my_module_1)
    # # my_module_1.my_module1.info_print1()
    # my_module1.info_print1()
    my_module_1.my_module1.info_print1()
