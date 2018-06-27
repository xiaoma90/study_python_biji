# 生成器就是一边循环一边计算的机制
# 第一种方法 只要把一个列表生成式的[] 改成 （） 就创建了一个generator
# 第二种方法  如果一个函数定义中包含yield 关键字，那么这个函数就不再是一个普通的函数，而是一个 generator:
# generator 和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator 的函数
# ，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('step 3')
#     yield 3
#     print('step 4')
#     yield 4
#
# o=odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))

#斐波那契
# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         print(b)
#         a,b = b,a+b
#         n=n+1
#     return 'done'
# fib(6)
# L = [x*x for x in range(10)]
# print(L)
#
# g = (x*x for x in range(10))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))