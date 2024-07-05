from threading import Thread


class SampleThread:
    def add(self, a, b):
        return a + b
    
class SampleThread1:
    num1 = 0
    num2 = 0
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2


s = SampleThread()
r = s.add(121,34)
print(r)


s1 = SampleThread1(10, 20)
r1 = s1.add()
print(r1)