from PizzaOrder import PizzaOrder

class OrderQueue:
    def __init__(self):
        self.heaplist = [0]
        self.crtsz = 0

    def addOrder(self, pizzaOrder):
        self.heaplist.append(pizzaOrder)
        self.crtsz += 1
        self.percup(self.crtsz)

    def percup(self,i):
        while i // 2 > 0:
            if self.heaplist[i].getTime() < self.heaplist[i // 2].getTime():
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2]
                self.heaplist[i // 2] = tmp
            i = i // 2


    def processNextOrder(self):
        if self.crtsz == 0:
            raise QueueEmptyException()
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.crtsz]
        self.crtsz -= 1
        self.heaplist.pop()
        self.percdown(1)
        return retval.getOrderDescription()

    def percdown(self,i):
        while 2*i <= self.crtsz:
            mc = self.minchild(i)
            if self.heaplist[i].getTime() > self.heaplist[mc].getTime():
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minchild(self, i):
        if i*2+1 > self.crtsz:
            return 2*i
        else:
            if self.heaplist[i*2].getTime() > self.heaplist[i*2 + 1].getTime():
                return 2*i + 1
            return 2*i
        

class QueueEmptyException(Exception):
    pass