import re

try:
    with open('text_6.txt', encoding='utf-8') as file:
        my_dict = {}
        my_list = []
        for line in file:
            my_list = re.findall('\\b\\d+\\b', line)
            names = re.findall(r'\w+', line)
            for i, item in enumerate(my_list):
                my_list[i] = int(item)
            my_list = sum(my_list)
            my_dict[names[0]] = my_list
        print(f'Formed a dictionary containing the name of the subject and the total number of lessons on it:\n{my_dict}')
except IOError:
    print('An I / O error has occurred!')
