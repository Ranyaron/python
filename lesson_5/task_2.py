with open('text.txt', encoding='utf-8') as file:
    strings = 0
    for line in file:
        words = 0
        strings += 1
        string = line.split()
        for i in string:
            words += 1
        print(f'Number of words per line {strings}: {words}')
    print(f'Number of lines in the file: {strings}')
