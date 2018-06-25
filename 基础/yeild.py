# 迭代器和生成器
# from collections import Iterable
#
# isinstance ('tony', Iterable)
# 通过 yield 返回的函数是一个生成器
# def nums(n):
#     a, b, c = 0, 1, 0
#     while True:
#         if c > n:
#             return
#         yield a  # 让这个函数变成一个生成器
#         a, b = b, a + b
#         c += 1
#
#
# tt = nums (10)
# print (type (tt))
# for t in tt:
#     print (t, end=" ")


# 装饰器 设计模式---装饰模式  @sum