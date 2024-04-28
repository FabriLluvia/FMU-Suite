def estrella(a):
    for row in range(a):
        for space in range(a - row - 1):  # Adjusting the number of spaces
            print(' ', end='')
        for star in range(row + 1):
            print('*', end='')
        for star in range(1, row + 1):
            print('*', end='')
        print()
    
    for row in range(a):  # Adjusted indentation
        for space in range(row):
            print(' ', end='')
        for star in range(a - row):
            print('*', end='')
        for star in range(a - row - 1):
            print('*', end='')
        print()
