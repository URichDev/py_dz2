#Дана строка. Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ, не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.

import string
import random

s = input('Enter the string: ')

def new_sstring(s):
    s_list = []

    i = 0
    while (len(s)>0) and (i<len(s)):
        letter_list = list(string.ascii_lowercase)

        fragment = s[i:i+3]
        letter_list.remove(fragment[0])
        letter_list.remove(fragment[2])
        let = letter_list[random.randint(1,len(letter_list))]

        fragment[1] = let

        s_list.append(fragment)
        i+=3
        print(fragment)

    print(s_list)

new_sstring(s)
