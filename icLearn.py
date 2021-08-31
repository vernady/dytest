from icecream import ic
from types import MethodType,FunctionType

class Foo(object):

    """类三种方法语法形成"""

    def instance_method(self):
        ic("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        ic("是静态方法")

    @classmethod
    def class_method(cls):

        ic("是类方法")

foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
ic('------------------------')
Foo.instance_method(1)
Foo.static_method()
Foo.class_method()
ic(isinstance(Foo.class_method,MethodType))
ic(isinstance(Foo.class_method,FunctionType))



class className:

    def method(self):
        print("这是一个方法")


# 调用---------------------
# 实例化对象
c = className()

c.method()

from types import MethodType, FunctionType


class Foo(object):
    def __init__(self):
        self.name = "haiyan"

    def func(self):
        print(self.name)


obj = Foo()
ic(isinstance(obj.func, FunctionType))  # False
ic(isinstance(obj.func, MethodType))  # True   #说明这是一个方法

ic(isinstance(Foo.func, FunctionType))  # True   #说明这是一个函数。
ic(isinstance(Foo.func, MethodType))  # False

alist = [1,2,3,4,5,6,7,8]

ic(alist)
del alist[2]
ic(alist)
