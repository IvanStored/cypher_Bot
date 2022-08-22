from string import *

abc_en = ascii_lowercase
abc_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def encrypt(text: str, k: int):  # This function encrypts message from user with the given key
    abc = abc_ru if text[0].lower() in abc_ru else abc_en
    result = []
    for char in text:
        if char.isupper():
            index = abc.index(char.lower())
            ni = index + k
            result.append(abc[ni % len(abc)].upper())
        elif char.islower():
            index = abc.index(char)
            ni = index + k
            result.append(abc[ni % len(abc)])
        else:
            result.append(char)
    return ''.join(result)


def decoding(text: str, k: int):  # This function decrypts message from user with the given key
    abc = abc_ru if text[0].lower() in abc_ru else abc_en
    result = []
    for char in text:
        if char.isupper():
            index = abc.index(char.lower())
            ni = index - k
            result.append(abc[ni % len(abc)].upper())
        elif char.islower():
            index = abc.index(char)
            ni = index - k
            result.append(abc[ni % len(abc)])
        else:
            result.append(char)
    return ''.join(result)
