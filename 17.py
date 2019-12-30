# Дана строка. Показать третий, шестой, девятый и так далее символы.

def find_3(s):
    s = s[2:]
    s = s[::3]
    print(s)

find_3('absdefghklmnoprst')