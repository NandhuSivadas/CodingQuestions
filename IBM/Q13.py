
#  License Plate Validation and Formatting

#  Problem Statement

# You are tasked with writing a function that validates and formats a license plate string.
#  The function must check the input string against several rules. If the string is valid, it should be converted to a standard format. 
# If it fails any validation rule, it should be marked as invalid.
#  Validation and Formatting Rules

# Your function must implement the following rules in order:

# 1.  Length Constraint: The initial input string must have a length between 2 and 10 characters, inclusive. If it's shorter than 2 or longer than 10, it's invalid 

# 2.  Allowed Characters: The string must only contain alphanumeric characters (A-Z, a-z, and 0-9). If it contains any special characters (like ``, `!`, `@`), it's invalid .

# 3.  Digit Requirement: The string must contain at least one digit (0-9). If it contains no digits, it's considered invalid

# 4.  Case Conversion: All lowercase letters in the string must be converted to uppercase

# 5.  Grouping and Formatting: After validation, the processed string should be divided into groups of characters separated by hyphens. The video's logic aims to create groups of three.
#      For example, a string like `ABC123XYZ` should become `ABC-123-XYZ`
#      An 8-character string like `ABC123XY` would be formatted as `ABC-123-XY`

#  Return Value

#  If the input string passes all validation checks, return the newly formatted string.
#  If the input string is invalid based on any of the conditions above, the function should return `"NA"` or `"INVALID"`

#  Sample Input and Output

# Sample 1 (Valid Input):
#  Input: `"aBc123xyz"`
#  Output: `"ABC-123-XYZ"`
#  Explanation: The string is 9 characters long, contains only alphanumeric characters, has digits, and is correctly formatted with hyphens after being converted to uppercase.

# Sample 2 (Valid Input with different length):
#  Input: `"ab123xy"`
#  Output: `"AB-123-XY"`
#  Explanation: The 7-character string is valid and formatted into groups.

# Sample 3 (Invalid Input - Special Character):
#  Input: `"ab@123xy"`
#  Output: `"NA"`
#  Explanation: The string contains a special character (`@`), making it invalid [[09:51](http://www.youtube.com/watch?v=iHpWMnIQVA4&t=591)].

# Sample 4 (Invalid Input - Too Long):
#  Input: `"ABC123XYZ00"`
#  Output: `"NA"`
#  Explanation: The string has 11 characters, which is more than the allowed maximum of 10 [[09:19](http://www.youtube.com/watch?v=iHpWMnIQVA4&t=559)].











import textwrap
def sol(plate):
    word=""
    if not plate.isalnum():
        return "NA"
    

    if len(plate)<2 or len(plate)>10:
        return "NA"
    
    if not any(i.isdigit() for i in plate):
        return "NA"

    
    word=plate.upper()
    return "-".join(textwrap.wrap(word,3))

    


plate="aBc123xyz"
print(sol(plate))