# Direct Recursion
# When a function calls itself directly
# Indirect Recursion
# When a function calls another function which calls the first function

# Direct Recursion
def recursion(n):
    if n == 0:
        return
    print("Hello")
    recursion(n - 1)

recursion(2)

# Indirect Recursion
def recursion2(n):
    if n == 0:
        return
    print("Hello")
    recursion(n - 1)

recursion2(2)

