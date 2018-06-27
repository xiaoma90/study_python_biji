#  协程 又称微线程  看上去是个函数，但执行过程中，在子程序内部可中断，然后转而执行别的函数，在适当的时候再返回来接着执行
#  特点：一个线程执行
#  优势: 1,极高的执行效率。因为子程序切换不是线程切换，而是程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势越明显
#      2， 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好
#  python 对协程的支持时通过generator实现的
#  在generator 中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但python的yield不但可以返回一个值，他还可以接受调用者发出的参数

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)