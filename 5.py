#Дана строка. Определить, содержит ли строка только символы 'a', 'b', 'c' или нет.

s = input('Type string: ')

def include_simbol(s):
    i=0
    k=0
    while i<len(s):
        if (s[i] != 'a') and (s[i] != 'b') and (s[i] != 'c'):
            print('The line contains characters not related to a, b, c')
            break
        else:
            k += 1
        i+=1

    if k == len(s):
        print('The string contains only a, b, с')

include_simbol(s)