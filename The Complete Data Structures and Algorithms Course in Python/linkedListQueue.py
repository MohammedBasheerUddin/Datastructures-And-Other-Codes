class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)
  
class linkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    currNode = self.head
    while currNode:
      yield currNode
      currNode = currNode.next

class Queue:
  def __init__(self):
    self.LL = linkedList()
  
  def __str__(self):
    values = [str(x) for x in self.LL]
    return ' '.join(values)
  
  def enqueue(self, value):
    newNode = Node(value)

    if self.LL.head == None:
      self.LL.head = newNode
      self.LL.tail = newNode
    else:
      self.LL.tail.next = newNode
      self.LL.tail = newNode
  
  def isEmpty(self):
    if self.LL.head == None:
      return True
    else:
      return False
    
  def dequeue(self):

    if self.isEmpty():
      return 'No elements present'
    else:
      temp = self.LL.head
      if self.LL.head == self.LL.tail:
        self.LL.head = None
        self.LL.tail = None
      else:
        self.LL.head = self.LL.head.next
      return temp

  def peek(self):
    if self.isEmpty():
      return 'No elements present'
    else:
      return self.LL.head


  def delete(self):
    self.LL.head = None
    self.LL.tail = None

qObj = Queue()
qObj.enqueue(1)
qObj.enqueue(2)
qObj.enqueue(3)
qObj.enqueue(4)
print('the elements inside queue are', qObj)
print('dequeue ', qObj.dequeue())
print('peek value is ', qObj.peek())
qObj.delete() # delete all the elements
print(qObj.isEmpty())

#output:
# the elements inside queue are 1 2 3 4
# dequeue  1
# peek value is  2
# True
