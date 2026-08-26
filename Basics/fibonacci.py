def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
for fibo in fibonacci(10):
    print(fibo)
