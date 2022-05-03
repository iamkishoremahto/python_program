# f = open("Kishore.txt")
# content =f.read()
# print(content)
# f.close()

f=open("Kishore.txt","r+")
# content  =f.read()
# for line in content:
#     # print(line)
#     print(line, end="")

# f.write("Kishore is a good boy")
# f.write("Kishore")
content=f.read()
for line in content:
    print(line, end="")