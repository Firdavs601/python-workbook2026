def caesar_cipher(text, shift):
    itog = ""
    
    for simvol in text:
        if simvol.isupper():
            a = ord(simvol) - ord('A')
            b = (a + shift) % 26
            v = b + ord('A')
            itog = itog + chr(v)
        elif simvol.islower():
            a = ord(simvol) - ord('a')
            b = (a + shift) % 26
            v = b + ord('a')
            itog = itog + chr(v)
        else:
            itog = itog + simvol
            
    return itog
