import math

n = int(input("Enter a number: "))

if n < 2:
    print(n, "is NOT Prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is Prime")
    else:
        print(n, "is NOT Prime")
