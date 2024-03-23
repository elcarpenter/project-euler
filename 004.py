def problem_four():
    """
    Find the largest palindrome made from the product
    of two 3-digit numbers.
    """
    palindrome = []
    for i in range(100, 1000):
        for j in range (110, 1000, 11):
            num = i * j
            if str(num) == str(num)[::-1]:
                palindrome.append(num)
    return max(palindrome)

print(problem_four())