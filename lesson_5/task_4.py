my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',
           'five': 'Пять', 'six': 'Шесть', 'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять'}

try:
    with open('text_4.txt', encoding='utf-8') as file:
        my_list = []
        for line in file:
            my_list.append(line.split())
        for i in my_list:
            for key, value in my_dict.items():
                if i[0] == key:
                    i[0] = value
                    break
except IOError:
    print('An I / O error has occurred!')

try:
    with open('text_44.txt', 'w', encoding='utf-8') as file:
        for el in my_list:
            file.writelines(' '.join(el) + '\n')
        print('English numbers have been replaced by Russians.\n'
              'The new block of lines is written to a new text file.')
except IOError:
    print('An I / O error has occurred!')
