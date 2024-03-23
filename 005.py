def problem_five():
    num = 2520
    check = 0
    while check != 20:
        check = 0
        num = num + 20
        for i in range(1, 21):
            if num % i == 0:
                check = check + 1
    return num

print(problem_five())