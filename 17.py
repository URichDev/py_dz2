# Дана строка. Показать третий, шестой, девятый и так далее символы.

s = input('Type string: ')

def find_3(s):
    s = s[2::3]
    print(s)

find_3(s)