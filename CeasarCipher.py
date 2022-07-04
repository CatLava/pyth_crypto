def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

key = generate_key(3)
print(key)
dkey = decryption_key(key)
message = "HELLO WORLD"
cipher = encrypt(key, message)
print(cipher)
# Want to break the cipher. How?
for i in range(26+1):
    dkey = generate_key(i)
    message1 = encrypt(dkey, cipher)
    print(message1, i)
