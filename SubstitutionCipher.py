from email import message
import random

def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key

def encrypt(key, message):
    encrypted = ""
    for l in message:
        if l == " ":
            encrypted += " "
        else:
            encrypted += key[l]
    return encrypted

def decrypt(key):
    dkey = {}
    for i in key:
        dkey[key[i]] = i
    return dkey

key = generate_key()
print(key)
mess = encrypt(key, "HELLOW WORLD")
print(mess)
nm = decrypt(key)
mess = encrypt(nm, mess)
print(mess)