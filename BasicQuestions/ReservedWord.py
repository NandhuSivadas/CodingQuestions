s="hello world"
def sol(s):
    word=s.split()
    return " ".join(reversed(word))


print(sol(s))