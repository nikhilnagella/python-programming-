import random
n=random.randint(1,100)
while True:
    print("Guess the number")
    x=int(input("Enter the number to match with random:"))
    if(x<n):
     print("too low")
    elif(x>n):
     print("too high")
    else:
     print("Your number is matched with the random")
