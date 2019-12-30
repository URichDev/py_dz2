# Написать функцию генерации email.
import string
import random

length = input('How long will the email be? ')
domein = input('What domain will the email have? ')

def gen_email(length, domain):
    letter_list = string.ascii_lowercase

    i=0
    s = ''
    while i<length:
        s += letter_list[random.randint(1,len(letter_list))]
        i += 1

    s += '@'+domain
    print(s)

gen_email(int(length), domein)