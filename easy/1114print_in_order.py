import time


class Foo(object):
    def __init__(self):
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond):
        time.sleep(0.1)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird):
        time.sleep(0.2)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
