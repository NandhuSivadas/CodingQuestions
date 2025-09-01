
# Question 2: Triangle Toy Validation
# In the assembly line, the factory assembles three parts a, b, c of a triangle toy. 
# A valid toy is one where the sum of the two shorter sides is greater than the longest side.

# There are two forms of valid triangles to identify:

# If two parts are of equal length, the form is "Isosceles".
# If all three parts are of equal length, the form is "Equilateral".
# If a toy is not valid or does not match one of these two forms, it is "None of these".

# Example:
# triangleToy = ['2 2 1', '3 3 3', '3 4 5', '1 1 3']
# First triangle: 2 2 1 → valid and has 2 equal parts → Isosceles
# Second triangle: 3 3 3 → valid and all 3 equal → Equilateral
# Third triangle: 3 4 5 → valid but neither of the two forms → None of these
# Fourth triangle: 1 1 3 → invalid because 1 + 1 ≤ 3 → None of these
# ✅ Sample Input:
# ['2 2 1', '3 3 3', '3 4 5', '1 1 3']
# ✅ Sample Output:
# ['Isosceles', 'Equilateral', 'None of these', 'None of these']


def sol(arr):
    res = []
    for t in arr:
        sides = list(map(int, t.split()))
        sides.sort()  
        
        if sides[0] + sides[1] <= sides[2]:
            res.append("None of these")
        elif sides[0] == sides[1] == sides[2]:
            res.append("Equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            res.append("Isosceles")
        else:
            res.append("None of these")
    return res

arr = ['2 2 1', '3 3 3', '3 4 5', '1 1 3']
print(sol(arr))
