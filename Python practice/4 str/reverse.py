# def reverseString(str1):
#     rev = ""
#     count = len(str1)
#     while count > 0:
#         rev += str1[count - 1]
#         count -= 1
#     return rev

# print(reverseString("Hello World"))

def reverseString2(str1):
    rev = ""
    for i in str1:
        rev = i + rev
    return rev

print(reverseString2("Hello World"))

def reverseString3(str1):
    rev = ""
    for i in range(len(str1)):
        rev = str1[len(str1) - i - 1] + rev
    return rev

print(reverseString3("Hello World"))