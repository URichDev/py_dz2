#Дана строка. Определите общее количество символов '+' и '-' в ней.
# А так же сколько таких символов, после которых следует цифра ноль.

s = input('Enter the string: ')

def count_simbols(s):
    count = 0
    special_count = 0
    i = 0
    while i<len(s):
        if (s[i] == '+') or (s[i] == '-'):
            count += 1
            if s[i+1] == '0':
                special_count += 1
        i +=1

    print(f"Number of characters + and -: {count}")
    print(f"Number of characters + and - with next '0' : {special_count}")
    # print(s)

count_simbols(s)