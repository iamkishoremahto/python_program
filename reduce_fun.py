from functools import reduce
list1=[1,5,4,6,8,5,4,2,1]

result= reduce(lambda x,y:x*y,list1)
print(result)