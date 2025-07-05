def simple(a, b, func):
    return func(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":
    print(simple(10, 20, add))
    print(simple(10, 20, sub))
    print(simple(10, 20, mul))
    print(simple(10, 20, div))