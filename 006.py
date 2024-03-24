def six():
    """
    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    """
    summa = 0
    for i in range(101):
        summa = summa + (i ** 2)
    sq_sums = ((100 * 101) / 2) ** 2
    return abs(sq_sums - summa)

print(six())