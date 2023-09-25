class Node:
    def __init__(self,isi):
        self._isi=isi
        self._next = None

class LL:
    def __init__(self):
        self._head =None

    def add1(self,isi):
        a=Node(isi)
        if self._head == None:
            self._head = a
        else:
            a._next = self._head
            self._head = a

    def cetak(self):
        a=self._head
        while a != None:
            print(a._isi)
            a=a._next

myLL= LL()
myLL.add1("a")
myLL.add1("b")
myLL.add1("c")

myLL.cetak()