import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

start = time.time()

result = fib(30)

end = time.time()

time_elapsed = end - start  # Time in seconds
print(f"Execution time: {time_elapsed:.6f} seconds")
print(f"Execution time: {time_elapsed * 1000:.2f} milliseconds")
print(f"Result: {result}")

