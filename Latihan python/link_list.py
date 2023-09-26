class Node:
    def __init__(self,dataval) -> None:
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        