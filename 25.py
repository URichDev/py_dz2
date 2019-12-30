# Дана строка. Вставить после каждого символа пробел.

s = input('Type string: ')

def insert_space(s):
    i = 0
    new_s = ''
    while i<len(s):
        new_s += s[i]+" "
        i+=1
    new_s.strip()
    print(new_s)

insert_space(s)