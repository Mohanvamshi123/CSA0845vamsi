listone = []
listtwo = []
print("enter 6 elements for the first list")
for i in range(6):
       listone.append(input())
print("enetr 6 elements for the second list")
for i in range(6):
       listtwo.append(input())

listthree = []
for i in range(6):
       listthree.append(listone[i])
for i in range(6):
       listthree.append(listtwo[i])
print("the new (merged) threelist is:")
print(listthree)
