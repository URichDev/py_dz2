#Дана строка. Вставить после каждого символа два случайных символа.
import string
import random

s = input('Type string: ')

def insert_simbols(s):
    letter_list = string.ascii_lowercase
    i = 0
    new_s = ''
    while i<len(s):
        new_s += s[i]
        new_s += letter_list[random.randint(1,len(letter_list))]
        new_s += letter_list[random.randint(1,len(letter_list))]
        i+=1
    new_s.strip()
    print(new_s)

insert_simbols(s)