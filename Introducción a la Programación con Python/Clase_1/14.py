#Fibonacci:
a0 = 0
a1 = 1
n = 10
for i in range(n):
    if i%2==0:
        print(a0)
        a0+=a1
    else:
        print(a1)
        a1+=a0
