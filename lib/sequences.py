#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    fibonacci_sequence = [0] * length
    if length > 0:
        fibonacci_sequence[0] = 0
    if length > 1:
        fibonacci_sequence[1] = 1

    for i in range(2, length):
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]

    print(fibonacci_sequence)