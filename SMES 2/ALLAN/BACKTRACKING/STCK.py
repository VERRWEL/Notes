class Node:
    def __init__(self):
        self.next = None
        self.data = input("masukkan data: ")

class Stack:
    def __init__(self):
        self.top = None
        
    def Push(self):
        NewNode = Node()
        if self.top == None:
            self.top = NewNode
        else:
            NewNode.next = self.top
            self.top = NewNode

    def IsEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    def ShowItems(self):
        temp = self.top
        if self.IsEmpty():
            print("stack is empty")
        else:
            while temp != None:
                print(f"{temp.data}\t")
                temp = temp.next


#main program
S = Stack()
S.Push()
S.Push()
S.Push()
S.Push()
S.ShowItems()
        