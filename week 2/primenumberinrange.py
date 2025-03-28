n = int(input("From where you want Prime Numbers: "))
end= int(input("Till where you want the Numbers: "))
for n in range(n, end + 1):
    if n <= 1:
        continue  
    for i in range(2, n):
        if n % i == 0:
            break  
    else:
        print(n, end=" ")
