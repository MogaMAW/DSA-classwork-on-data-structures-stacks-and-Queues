class Stack():
    def __init__(self):
         self.items = [1,3,4,3,64,89]
    def is_empty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peak(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __repr__(self):
        return "Greatest value: {}, size :{}".format(self.peak(),self.size())
""" reverses a  stack"""
PROMPT = "Enter an int value (<0 to end):"
myStack = Stack()
value = int(input( PROMPT ))
while value >= 0 :
    myStack.push( value )
    value = int(input( PROMPT ))
while not myStack.is_empty() :#when a negative integer is entered,the loop displays a reversed stack
    value = myStack.pop()
    print( value )
