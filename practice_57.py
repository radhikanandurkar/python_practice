outer_list =[]
for i in range(3):
    inner_list =[]
    for j in range(2):
        v=int(input("enter value: "))
        inner_list.append(v)

    outer_list.append(inner_list)
    print(outer_list)
    print(v)