def estrella(a):
    for row in range(a):
        for _ in range(a - row - 1):  # Adjusting the number of spaces
            print(' ', end='')
        for _ in range(row + 1):
            print('*', end='')
        for _ in range(1, row + 1):
            print('*', end='')
        print()
    
    for row in range(a):  # Adjusted indentation
        for _ in range(row):
            print(' ', end='')
        for star in range(a - row):
            print('*', end='')
        for star in range(a - row - 1):
            print('*', end='')
        print()
