__all__ = ['testD', 'testA']


def testA(a, b):
    print(a - b)


def testB(a, b):
    print(a + b)


def testC(a, b):
    print(a * b)


def testD(a, b, *args):
    return a ** b
