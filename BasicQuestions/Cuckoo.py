# Problem Statement:
# Write a function to generate the n-th term in a special sequence known as the "Cuckoo Sequence", defined as:
# Let cuckoo1 = 0, cuckoo2 = 1
# For each term from 0 to n-1, the sequence follows the rule:
# cuckoo3 = cuckoo2 + 2 * cuckoo1 + 3 * 1

def cuckoo(n):
    cuckoo1 = 0
    cuckoo2 = 1

    if n == 1:
        print(cuckoo1)
    elif n == 2:
        print(cuckoo2)
    else:
        for i in range(3, n + 1):
            cuckoo3 = cuckoo2 + 2 * cuckoo1 + 3 * 1
            cuckoo1 = cuckoo2
            cuckoo2 = cuckoo3
        print(cuckoo3)


n = int(input("Enter the nth term: "))
cuckoo(n)
