n = int(input("No. of fibonacci patterns:"))
a = 0
print(a,end = " ")
b = 1
print(b,end = " ")
while (n > 0):
    c = a+b
    print(c,end = " ")
    a = b
    b = c
    n = n - 1
