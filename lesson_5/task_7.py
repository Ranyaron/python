import re
import json

try:
    with open('text_7.txt', encoding='utf-8') as file:
        my_dict = {}
        my_list = []
        e = 0
        for line in file:
            line_file = line.split()
            numbers = re.findall('\\b\\d+\\b', line)
            for i, item in enumerate(numbers):
                numbers[i] = int(item)
            numbers = numbers[0] - numbers[1]
            my_dict[line_file[0]] = numbers
        for key, value in my_dict.items():
            if value > 0:
                my_list.append(value)
                e += 1
        average_profit = {'average_profit': round((sum(my_list) / e), 2)}
        print(f'Average profit of companies, excluding unprofitable ones = {round((sum(my_list) / e), 2)}')
except IOError:
    print('An I / O error has occurred!')

my_list_full = [my_dict, average_profit]

try:
    with open('text_777.json', 'w', encoding='utf-8') as file:
        json.dump(my_list_full, file, indent=4, ensure_ascii=False)
        print('A list containing a dictionary with firms and their profits / losses,\n'
              'as well as a dictionary with an average profit is saved as a json object to a file.')
except IOError:
    print('An I / O error has occurred!')
