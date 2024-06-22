userReply = input("Would you like juice,biscuit or cake? (Enter juice,biscuit,cake or nothing) ")
if userReply == "juice":
    print("here is your drink")
elif userReply == "biscuit":
        print("here is our snack")
elif userReply == "cake":
        cake= input("Which cake?(Enter blackforest,whiteforest)")
        print("here is your {}cake".format(cake))
else:
        print("Have a good day")
        
