print('Enter data line by line. The end of data entry is indicated by an empty line.')

while True:
    file = input()
    if file == '':
        break
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(f'{file}\n')
