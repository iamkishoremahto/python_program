from lib2to3.pgen2.pgen import DFAState


List = [1,5,4,6,9,8,5,2,10,2,40,5,10,15,25]

def Greater_than_5(num):

    return num>5

gr_th_5=list(filter(Greater_than_5,List))
print(gr_th_5)


