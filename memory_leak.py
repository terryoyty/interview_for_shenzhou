# -*- coding:utf-8 -*-
# author:   terry
# email:   terryoyty@163.com
# datetime: 2022/06/15 13:09
# ide:      PyCharm


"""
请简述内存泄漏的含义？

内存泄漏是指在程序运行结束后，对象的申请内存空间没有得到正常释放，从而使该空间长期被占用。
"""

"""
使用python，写出一段具有内存泄漏的代码
"""


class MemoryLeakDemo:

    def __init__(self):
        self.some_attr = None

    def __del__(self):
        print('do something...')


demo_obj_1 = MemoryLeakDemo()
demo_obj_2 = MemoryLeakDemo()
demo_obj_1.some_attr = demo_obj_2
demo_obj_2.some_attr = demo_obj_1

"""
简述为什么会内存泄露

1.因为对象存在循环引用，导致引用计数始终不能为0，引用计数回收机制无法处理
2.因为定义了__del__方法，导致标记清楚算法无法计算该对象，标记清楚回收机制无法处理
"""
