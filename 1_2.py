numbers = []
for i in range(1, 1001, 2):
    numbers.append(i ** 3)
print(numbers)

b = []
coub_sum = 0
for n in numbers:
    i = n
    while n != 0:
        coub_sum += n % 10
        n = n // 10
    if coub_sum % 7 == 0:
        b.append(i)
    coub_sum = 0
print(sum(b))

sum_all_coub = 0
for n in numbers:
    coub_sum = 0
    i = n
    n += 17
    while n != 0:
        coub_sum += n % 10
        n = n // 10
    if coub_sum % 7 == 0:
        sum_all_coub += i
print(sum_all_coub)