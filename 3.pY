def sum_of_digits(n):
    total = sum(int(digit) for digit in str(n))
    return total

#example
print(sum_of_digits(123455655))