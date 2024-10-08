
class Node:
  def __init__(self):
    self.data = input("Input Data: ")
    self.next = None

class StackLL:
  def __init__(self):
    self.top = None

  def IsEmpty(self):
    if (self.top == None):
      return True
    else:
      return False

  def Push(self):
    newNode = Node()
    if self.IsEmpty():
      self.top = newNode
    else:
      newNode.next = self.top
      self.top = newNode
    print(f"Data '{newNode.data}' is successfully added!")

  def Pop(self):
    if self.IsEmpty():
      print("Cannot delete any data because Stack is empty!")
    else:
      temp = self.top
      self.top = self.top.next
      temp.next = None
      print(f"Data '{temp.data}' is successfully removed!")

  def Clear(self):
    self.top = None
    print("Stack is successfully cleared!")

  def PrintStack(self):
    temp = self.top
    if self.IsEmpty():
      print("Stack is empty!")
    else:
      while (temp != None):
        print(f"[{temp.data}\t]")
        temp = temp.next

  def PrintTop(self):
    if self.IsEmpty():
      print("Top: None")
    else:
      print("Top:", self.top.data)

S1 = StackLL()
while True:
    inp = int(input("1. Push\n2. Pop\n3. Clear\n4. Print Stack\n5. Print Top\n6. Exit\nInput: "))
    if inp == 1:
        S1.Push()
    elif inp == 2:
        S1.Pop()
    elif inp == 3:
        S1.Clear()
    elif inp == 4:
        S1.PrintStack()
    elif inp == 5:
        S1.PrintTop()
    else:
        break
