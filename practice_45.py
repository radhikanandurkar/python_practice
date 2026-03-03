# Print Fibonacci series.
num = int(input("enter number : "))
a=0
b=1
fibonacci =0
while fibonacci<num: 
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    fibonacci+=1
