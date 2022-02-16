import string
import re

def reverse(text):
    '''for p in string.punctuation:
        if p in text:
            text.replace(p, "")'''
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)


while True:
    something = input('Введите текст: ')
    line = re.sub('[!@#$\n-., ]', '', something)
    line = line.upper()
    if (is_palindrome(line)):
        print("Да, это палиндром")
        print(something, line)
        break
    else:
        print("Нет, это не палиндром")
        continue