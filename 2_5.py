price_list = [69.8, 92.53, 90.95, 95.16, 652.20, 66.8, 37.74, 49.01, 97.84,
              47.88, 77.34, 4.77, 80.26, 32.37, 204.5, 67.50, 8.27, 74.56, 108.69]

print(' Пункт "A"')
for i in price_list:
    print(f'{int(i)}руб.{int(i * 100 % 100):02d}коп; ', end=' ')

print('\n Пункт "B"')
print(id(price_list), price_list)
price_list.sort()
print(id(price_list), price_list)


print(' Пункт "С"')
price_list2 = price_list[::-1]
print(id(price_list2), price_list2)

print(' Пункт "D"')
print(price_list2[:5])