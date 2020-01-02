#Написать генерацию строк длины 10, причем первые 4 символа - цифры, следующие два символы - различные буквы,
# следующие 4 символа - нули или единицы, причем одна единица точно присутствует.

import string
import random

def gen_str():
    s = ''
    length_str = 10
    num_simbol = 4
    let_simbol = 2
    bool_simbol = 4

    letter_list = string.ascii_lowercase

    i = 0
    while i<num_simbol:
        s += str(random.randint(0,9))
        i+=1

    i = 0
    while i<let_simbol:
        s += letter_list[random.randint(1,len(letter_list))]
        i += 1

    i = 0
    ss = ""
    while i<bool_simbol:
        ss +=  str(random.randint(0,1))
        i+=1

    if ss.find('1') != -1:
        s += ss
    else:
        ss[random.randint(0,bool_simbol-1)] = 1
        s += ss

    print(s)


gen_str()