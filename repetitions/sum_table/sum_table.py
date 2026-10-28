for j in range(0, 10):
    for i in range(0 + j, 10 + j):
        if i >= 10:
            print(i, end=' ')
        else:
            print(i, end='  ')
    print(end='\n')