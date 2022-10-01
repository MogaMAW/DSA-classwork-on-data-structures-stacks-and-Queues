# import random
# a=[]
# n=int(input("Enter number of elements:"))
# for j in range(n):
#     a.append(random.randint(1,20))
# print('Randomised list is: ',a)

# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l)
		
# printValues()
		
# class MyIterator:
#     def __init__(self, max):
#         self.max = max
#         self.curr = 0
#     def __next__(self):
#         if self.curr < self.max:
#             ret = self.curr
#             self.curr += 1
#             return ret
#         else:
#             raise StopIteration()
#     def __iter__(self):
#         return self
# it = MyIterator(10)
# for i in it:
#  print(i, end=' ')

# lst = [x+y for x in ['a','the','one']
#  for y in [' car',' fish']] 
# print(lst)

