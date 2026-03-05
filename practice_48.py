# Print prime numbers 1–100.
for n in range(2,101):
    for i in range(1,n):
        if n%i==0:
            break
    else:
        print(n)