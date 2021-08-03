for proc in range(1,101):
    if (10 < proc < 20) or (proc % 10 in [0, 5, 6, 7, 8, 9]):
        print(proc, 'процентов')
    elif proc % 10 ==1:
        print(proc, 'процент')
    else:
        print(proc, 'процента')