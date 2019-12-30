# Удалить в строке все лишние пробелы, то есть серии подряд идущих пробелов заменить на одиночные пробелы.
# Крайние пробелы в строке удалить.

s = input('Type string: ')

def clear_space(s):
    s = s.split(' ')
    new_s = ''
    for item in s:
        if item != '':
            new_s += item
            new_s += ' '
    print(new_s)

clear_space(s)
