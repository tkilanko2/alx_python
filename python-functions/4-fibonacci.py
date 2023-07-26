def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(n - 2)]
    return fib_sequence[:n]
