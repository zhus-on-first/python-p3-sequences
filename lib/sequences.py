#!/usr/bin/env python3

def print_fibonacci(length):
    # next number is found by adding up the two numbers before it
    if length <= 0: 
        print([])
        return
    
    if length == 1:
        print([0])
        return
    
    #initialize list with first 2 numbers
    fib_sequence = [0, 1]

    #dynamically set others
    for num in range(2, length):
        next_number = fib_sequence[num - 1] + fib_sequence[num - 2]
        fib_sequence.append(next_number)

    print(fib_sequence)