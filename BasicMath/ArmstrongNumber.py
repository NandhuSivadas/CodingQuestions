n=int(input("Enter:"))
temp=n
arm=0
while n:
    d=n%10
    arm+=d*d*d
    n=n//10

if arm==temp:
    print("Armstrong")
else:
    print("Not Armstrong")
