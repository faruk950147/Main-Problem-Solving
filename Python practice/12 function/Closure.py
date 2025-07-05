# Closure in Python (Function Closures)
# Closure means:
# A inner function, which can hold outer function's variable or state, even after outer function execution has finished.
# Example:

# jodi outer function er variable k inner function er moddhe hold kore rakhe

def outer(x):
    def inner(y):
        return x + y
    return inner

closure_func = outer(10)
print(closure_func(5))   # Output: 15

# Here closure_func is a closure, because it holds the value of x=10 in memory.
