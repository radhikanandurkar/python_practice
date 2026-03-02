# Calculator using if-else (+ − × ÷).
opretion = input("enter opretion: ")
a= 4
b= 6
add = a+b
sub = a-b
div = a/b
multi = a*b
if opretion =="add":
    print(add)
elif opretion == "sub":
    print(sub)
elif opretion == "div":
    print(div)
elif opretion == "multi":
    print(multi)
else:
    print("invalid opretion ")