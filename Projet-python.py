import sys
import base64
def main():
    menu()
def codage64():
    print("**CODAGE 64**")
    m=input("Enter le message à coder : ")
    m_bytes = m.encode('ascii')
    base64_bytes = base64.b64encode(m_bytes)
    message_codé = base64_bytes.decode('ascii')
    print("\n Le message codé est : ",message_codé)
    print("")
    codage()
def decodage64():
    print("**DECODAGE 64")
    m=input("Enter le message à décoder : ")
    base64_bytes = m.encode('ascii')
    m_bytes = base64.b64decode(base64_bytes)
    message_decodé = m_bytes.decode('ascii')
    print("\n Le message décode : ",message_decodé)
    print("")
    codage()
def codage():
    while True:
        print("1) CODAGE")
        try:
            choix = input( """ 
                         A-Codage en base 64
                         B-Decodage en base 64
                         C-Retour au menu principal  
                         Choix: """)
            break
        except ValueError:
            print("Entrer invalide")
    if choix == 'A' :
        codage64()
    elif choix == 'B' :
        decodage64()
    elif choix == 'C' :
        menu()
    else:
        print("choix invalide ! réessayer ")
        codage()
def clef():
    while True:
        try:
            x=int(input("donner la Clef entre 30 et 1000 : "))
            if x >= 30 and x <= 1000:
                break
            else :
                print("Clef non valide !!")
        except ValueError:
            print("Input invalide")
    return (x)


def chiffrer_letter(letter, is_upper, decaler):
    if is_upper:
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    else:
        l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    crypted_index = (l.index(letter) + (decaler % 26)) % 26
    return l[crypted_index]


def dechiffrer_letter(letter, is_upper, decaler):
    if is_upper:
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    else:
        l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    decrypted_index = (l.index(letter) - (decaler % 26)) % 26
    return l[decrypted_index]


def chiffrer():
    print("**CHIFFRER**")
    c = clef()
    m= input("Message à chiffrer: ")
    crypted = list()
    for letter in m:
        if letter.isalpha():
            up = letter.isupper()
            crypted_letter = chiffrer_letter(letter, up, c)
            crypted.append(crypted_letter)
        else:
            crypted.append(letter)
    crypted = ''.join(crypted)
    print("\nMessage chiffré:", crypted)
    chiffrement()
def dechiffrer():
    print("DECHIFFER")
    c = clef()
    m = input("Message à dechiffrer: ")
    decrypted = list()
    for letter in m:
        if letter.isalpha():
            up = letter.isupper()
            decrypted_letter = dechiffrer_letter(letter, up, c)
            decrypted.append(decrypted_letter)
        else:
            decrypted.append(letter)
    decrypted = ''.join(decrypted)
    print("\nMessage déchiffré:", decrypted)
    chiffrement()


def chiffrement():
    while True:
        print("2) CHIFFREMENT")
        try:
            choix =input("""
                        A-Chiffrer un message par une clef
                        B-Dechiffrer un message par une clef
                        C-Retour au menu principal
                        Choix: """)
            break
        except ValueError:
            print("Entrer invalide")
    if choix == 'A':
        chiffrer()
    elif choix == 'B':
        dechiffrer()
    elif choix == 'C':
        menu()
    else:
        print("choix invalide")
        chiffrement()
def quitter():
    a=input("si vous voulez quitter taper 'Q' ")
    if a=='Q' or a=='q' :
        sys.exit
    else:
        menu()
def menu():
    print("Outil de Decodage et de Chiffrement")
    while True:
        try:
            choix = int(  input( """
                         1-Codage
                         2-Chiffrement
                         3-Quitter
                         Choix: """
                                ))
            break
        except ValueError:
            menu()
    if choix == 1:
        codage()
    elif choix == 2:
        chiffrement()
    elif choix == 3:
        quitter()
    else:
        menu()
main()








