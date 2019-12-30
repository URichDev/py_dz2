#В данной строке вставить после каждого символа 'a' символ 'b'.

s = input('Type string: ')

def insert_simbol(s):
    s = s.replace('a','ab')
    print(s)

insert_simbol(s)