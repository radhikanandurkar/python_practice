#WAP Find common elements in two lists
l1 = [1,2,3,4,5,7,8]
l2 = [34,5,66,345,1,3,8,7]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

