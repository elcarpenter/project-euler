def problem_two():
    """
    By considering the terms in the Fibonacci
    sequence whose values do not exceed four
    million, find the sum of the even-valued terms.
    """
    x = 1
    y = 1
    summa = 0
    while x + y < 4000000:
        _next = x + y
        x = y
        y = _next
        if y % 2 == 0:
            summa = y + summa
    return summa

print(problem_two())