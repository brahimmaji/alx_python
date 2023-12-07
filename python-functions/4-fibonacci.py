def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacci = [0, 1]
        for i in range(2, n):
            next_number = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(next_number)
        return fibonacci