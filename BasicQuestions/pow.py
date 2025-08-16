# Check if number is power of two.

# Test: 16→True, 18→False
def pow1(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0  


print(pow1(16))  
print(pow1(18)) 