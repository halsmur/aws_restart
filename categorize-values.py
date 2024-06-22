mylist=[45,"wonder",False,"65"]
print(mylist)
for item in mylist:
    print("{} is of the data type {}".format(item,type(item)))
mylist.append(80)
print(mylist)