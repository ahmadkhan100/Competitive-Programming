def simulate_algorithm(n):
    # Start with the initial value of n
    sequence = [n]

    # Continue modifying n until it becomes 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)  # Append each new value of n to the list

    # Return the list of values in the sequence
    return sequence
