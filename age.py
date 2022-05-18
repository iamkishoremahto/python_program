user_input= input("Enter your age or year of birth : ")
if len(user_input)<=3:
    year_of_birth= 2022-int(user_input)
    af_100= year_of_birth +100
elif len(user_input)<=4:
    af_100= int(user_input) + 100
elif len(user_input)>4:
    print("Please enter a valid year")
    af_100=None
if(af_100 == None):

    print(" ")
else:
    print(f"In {af_100} you will turn 100 years")