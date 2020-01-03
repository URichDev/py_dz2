#Даны две строки. Определите, можно ли из некоторых символов первой строки и всех символов второй строки
# составить новую строку, в которой каждый символ встречается ровно два раза.

s1 = input('Enter the string 1: ')
s2 = input('Enter the string 2: ')

def new_str(s1,s2):
    s3 = s1+s2
    for item in s3:
        item_count = s3.count(item)
        if item_count%2 != 0:
            result = False
            break
        else:
            result = True

    if result == True:
        print(s3)
    else:
        print('False')

new_str(s1,s2)