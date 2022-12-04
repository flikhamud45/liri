def decode_pass(pw):
    return "".join([chr(ord(char)+2) if char.isalpha() else char for char in pw ])
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print (decode_pass(password))