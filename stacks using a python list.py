class Stack():
    def __init__(self):
         self.items = [1,3,4,56,6]
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
Class = Stack()
print(Class.is_empty())
Class.push(2)
Class.push(5)
Class.push(8)
print(Class.is_empty())
print(Class.peak())
print(Class.size())