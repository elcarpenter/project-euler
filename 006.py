def six():
    """
    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    """
    summa = sum([i ** 2 for i in range(101)])
    sq_summa = ((100 * 101) / 2) ** 2
    return abs(sq_summa - summa)

print(six())