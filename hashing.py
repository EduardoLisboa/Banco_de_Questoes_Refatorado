from math import factorial

hasheado = list()
def hashing(to_hash):
    for i in to_hash:
        hasheado.append(str(factorial(ord(i) % 13)))
    
    pronto = ''.join(hasheado)
    hasheado.clear()
    return pronto
