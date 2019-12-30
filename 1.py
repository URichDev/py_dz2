# Написать функцию генерации email.
import string
import random

def gen_email(length, domain):
    letter_list = string.ascii_lowercase

    i=0
    s = ''
    while i<length:
        s += letter_list[random.randint(1,len(letter_list))]
        i += 1

    s += '@'+domain
    print(s)

gen_email(10, 'gmail.com')