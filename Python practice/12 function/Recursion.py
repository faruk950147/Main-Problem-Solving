
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)
print(recursive_sum(5))

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)
print(recursive_factorial(5))

def sayHello(n):
    if n == 0:
        return
    print("Hello")
    sayHello(n - 1)
sayHello(5)