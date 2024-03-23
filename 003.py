def problem_three():
    """
    What is the largest prime factor of the number
    600851475143?
    """
    factors = []
    x = 600851475143
    d = 2
    while x > 1:
        while x % d == 0:
            factors.append(d)
            x = x / d
        d = d + 1
        if d * d > x:
            if x > 1:
                factors.append(x)
                break
    return max(factors)

print(problem_three())
