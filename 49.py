#Найдите количество вхождения 'aba' в строку.

s = input('Type string: ')

def find_str(s):
    list_str = s.split('aba')
    if len(list_str)>0:
        print(len(list_str)-1)
    else:
        print('0')

find_str(s)