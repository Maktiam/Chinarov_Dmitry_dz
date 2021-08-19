def odd_number(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_10 = odd_number(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(odd_to_10)