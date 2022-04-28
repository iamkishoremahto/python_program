items=["kishore",int,float,7,5,6,9,8,7,8,12,45]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)