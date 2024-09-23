import hashlib
import time

print("""

⠐⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⡠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⢠⠀⠄⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⠂
⠂⠄⡁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠐⠠⠁⠌⠠⠁⢌⣠⣁⣌⣤⣡⣌⣤⣥⣬⣤⣥⣬⣤⣥⣬⣄⣡⣌⣤⣁⣌⡠⠉⡐⠠⢈⠐⠠⢁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠄⡁
⡁⠂⠄⠡⢈⠐⠠⢈⠐⠄⠠⠁⠌⡐⠠⢁⣂⣥⠾⠒⠛⡉⠡⠀⠄⡀⠄⡀⠠⢀⠠⠀⠄⠠⠀⠄⡀⠠⢀⠠⠀⠄⡈⢉⠛⠒⠶⣤⣈⠐⠠⠈⠄⡁⠂⠌⡐⠠⢀⠡⢈⠐⡀⠂⠄
⠄⠡⢈⠐⠠⢈⠐⠠⠈⠄⠡⠘⠠⠐⣠⠞⡁⠠⠐⡈⠐⠠⠁⠌⡐⢀⠂⠄⡁⠂⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⢂⠐⠄⣈⠐⠠⠀⠌⠳⣆⢁⠂⠄⡁⠂⠄⡁⢂⠐⡀⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⠈⠄⠡⠈⢄⠁⢂⢱⠇⡐⠠⢁⠂⠄⡁⢂⠁⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⠂⠄⡁⠂⠄⡁⢂⠐⠠⢈⠐⠠⢈⠡⠈⠄⠡⠸⡆⡈⠐⠠⢁⠂⡐⢀⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠌⡀⡟⠠⢀⠡⠀⠌⣐⣀⣂⡌⡠⢈⠐⠠⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⡐⠠⢈⡐⣠⣈⣐⣀⠂⠡⠈⠄⡁⢿⠀⡁⠂⠄⢂⠐⠠⢈⠐⠠⢁⠂⠄
⡁⠂⠄⠡⠈⠄⠡⢈⠐⠠⠌⡐⢠⡇⢁⠂⢤⡷⣿⣭⣿⣿⣿⣿⣿⣶⢥⣌⠠⢁⠂⠌⡐⠠⢈⠐⡀⣢⡴⣷⣿⣿⣿⣿⣿⣭⣿⢦⡅⢂⠐⢸⠂⠄⠡⠈⠄⣈⠐⠠⢈⠐⠠⠈⠄
⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠄⡐⢠⡇⠠⢨⣯⠿⠋⢉⠉⡉⠙⠻⠿⣿⣿⣿⣭⠂⠌⡐⠠⢁⠂⡐⣭⣷⣿⣿⠿⠟⠋⢉⠉⡉⠙⠿⣽⡆⢈⢸⡃⠌⠠⢁⠂⠄⡈⢐⠠⠈⠄⡁⠂
⠌⠠⠁⠌⡐⠠⢈⠐⠠⢈⠐⠠⢸⠇⡀⡏⠁⠄⡈⠄⠂⠄⡁⢂⠐⡈⠙⠻⠟⠃⡐⠠⢁⠂⡐⠈⠿⠟⠋⡁⠐⠠⢁⠂⡐⠠⢁⠂⠌⢹⠀⢸⡇⠠⢁⠂⠌⡐⢀⠂⠄⡁⠂⠄⡁
⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢈⠐⣸⡁⢣⠁⠌⡐⠠⢈⣰⣤⣴⣤⣦⣄⡁⠂⠌⠠⢹⡆⢀⢢⡟⠀⢂⠐⢠⣠⣥⣦⣤⣦⣀⠁⠂⠌⡐⠈⣜⠠⡇⠂⠄⡈⠐⡀⠂⠌⡐⠠⢁⠂⠄
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⢂⠐⣾⠀⡘⣧⡂⠠⣱⡟⣫⣭⣶⣾⣯⣽⣛⢷⡌⠐⣀⡇⠂⢼⡀⠌⢠⡾⢟⣯⣽⣶⣾⣭⣝⣻⣦⠂⢠⣽⠁⠄⣿⢀⠂⠌⡐⠠⢁⠂⠄⡁⠂⠌⡀
⠂⠄⡁⠂⠌⡐⠠⢈⠐⡀⠂⢄⡏⡐⢀⣬⣷⣿⣿⣜⣛⠿⠿⠿⠿⣛⣻⡼⠋⠠⢸⡇⢈⢸⡇⠠⠙⣷⣟⣻⠿⠿⠿⢿⣛⣣⣿⣿⣾⣅⡀⢂⢹⡠⢈⠐⠠⢁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠸⣇⣰⣿⠞⠉⡀⠄⡉⠛⠛⠛⠛⠛⢋⠡⢀⠁⢂⢸⡇⠠⢸⡇⠠⢁⠠⢈⠙⠛⠛⠛⠛⠛⠉⡀⠄⡉⠺⣽⣆⣼⡃⠠⢈⠐⠠⢈⠐⠠⢁⠂⠌⡀
⠄⡁⠂⠄⡁⠂⠄⠡⢈⠡⢀⠸⣿⠴⠁⡀⢂⠐⠠⠄⠡⠈⠄⠡⠈⠄⠂⠄⡈⠄⣾⠁⡐⠈⣷⠐⡀⠂⠤⠈⠄⠡⠈⠄⡁⢂⠐⢠⠀⠡⠈⠧⣿⠆⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡀
⠂⠄⡁⠂⠄⠡⢈⠐⡀⠆⠠⢘⣿⡆⡐⡀⠂⠌⡐⠈⠄⠡⠈⠄⠡⢈⣰⠀⡐⢸⡏⠐⠠⢁⢹⡇⠠⢁⣂⠡⠈⠄⡁⢂⠐⠠⠈⠄⡈⠄⢡⢸⣿⠂⠄⡈⠐⠠⢁⠂⠌⡐⢀⠂⠄
⡁⠂⠄⠡⢈⠐⡀⢂⠐⡈⠐⡀⢿⢷⡹⣦⣁⠂⠄⠡⠈⠄⢡⣨⣴⣾⡇⠐⠠⢸⠂⡁⠂⠄⣈⡇⠐⠠⢹⣷⣮⣔⠀⠂⠌⠠⢁⠂⣐⣼⢏⡾⡿⢀⠂⠄⡑⢀⠂⠌⡐⢀⠂⠌⡀
⠄⠡⢈⠐⡀⢂⠐⡀⠂⠌⡐⢀⠺⡏⣧⣨⣿⡷⣾⣤⣷⠾⠛⠋⡁⠘⢧⣈⣴⣬⣣⠠⢁⠂⡜⣥⣼⣀⡼⠃⡈⠙⠻⠷⣾⣴⣶⢾⣿⣅⣼⢱⡇⠠⢈⠐⡀⠂⠌⡐⢀⠂⠌⡐⠀
⠌⡐⢀⠂⡐⢀⠂⠄⡁⠂⠔⠠⠈⣧⠘⣧⣻⣷⡜⣿⣿⣧⡠⠁⠄⡁⠂⠌⣹⣿⣿⣿⣿⣿⣿⣿⣏⠁⠄⠂⠄⡁⢂⣼⣿⣿⢣⣾⡿⣼⠃⣼⠀⡁⢂⠐⠠⢁⠂⡐⠠⢈⠐⠠⠁
⢂⠐⡀⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⢹⡄⠘⣧⣳⡿⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡿⣡⢿⢟⡼⠁⢤⡏⠐⡀⠂⠌⡐⢀⠂⠄⡁⠂⠌⠠⠁
⢂⠐⡀⠂⠌⡐⠠⠈⠄⠡⢈⡐⠠⢈⣧⠐⠈⢷⡻⣝⢦⣙⠛⠛⠛⠛⠛⠛⠛⠿⠿⣤⢥⡬⠽⠟⠛⠛⠛⠛⠛⠛⠛⢋⡴⣫⢟⡾⠁⠌⣸⠁⠂⠄⡁⢂⠐⠠⢈⠐⠠⠁⠌⠠⠁
⢂⠐⠠⢁⠂⠄⠡⠈⠄⡁⠂⠄⡁⢂⠸⣆⠁⢂⠻⣝⢦⡙⠲⣬⣀⠡⠈⠄⡁⠂⠄⠠⢀⠀⠂⠌⠠⠁⠌⢠⣁⣬⠞⢋⡴⣫⠟⠀⠌⣰⠋⠄⡁⢂⠐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁
⠂⠌⡐⠠⠈⠄⠡⢈⠐⠠⢁⠂⠰⢀⠂⠙⣎⡠⢀⠛⣮⢳⡄⠠⢉⠙⠛⠛⠓⢻⣶⣷⣶⣾⣾⡞⠛⠛⠛⠋⢉⠀⣐⠞⣵⠋⠠⢁⣼⠋⢀⠂⡐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠄
⡁⠂⠄⠡⠈⠄⡁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡈⠳⣄⠂⡈⢷⡙⢦⠀⠌⠠⢁⠂⠄⣿⣿⣿⣿⣿⠀⡐⠠⠁⠌⡀⡲⢋⡾⠁⠠⣡⠞⢁⠀⢂⠐⠠⢁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂
⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂⠌⡐⠀⠆⠠⢁⠘⠷⣄⠀⠻⣦⠋⠠⢁⠂⠌⡐⣿⣿⣿⣿⣿⠃⠠⠁⠌⡐⠘⣵⠋⠄⣈⡶⠉⡐⠠⠈⠄⣈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠌⡐⠠⠁
⠌⠠⢁⠂⠄⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠐⠄⠂⠄⡉⠷⣄⡈⢷⡅⠂⠌⡐⢀⢹⣿⣿⣿⡏⠠⠁⠌⡐⢠⡟⢁⣰⠞⢉⠀⡐⠠⠁⠌⡐⠠⠈⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠄⠡⢈⠐⠠⠈⠄⡑⠠⠐⠠⢈⠻⢤⡙⢧⡐⢀⠂⠄⣿⣿⣿⠀⢂⠁⢂⡴⢋⡴⠞⠁⡐⢀⠂⠄⠡⢈⠐⠠⠁⠌⠠⠁⠌⡐⠠⢁⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⡐⠠⢈⠐⠠⠁⠌⡐⠠⠈⠄⡁⠂⠄⠡⢈⠐⡠⠐⠠⠙⠲⢽⡦⢬⣀⢿⣿⡿⣀⡦⢼⡯⠖⠋⡀⢂⠡⠐⠠⠈⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠌⠠⢁⠂⠄⠡⢈⠐⠠⠁⠌⡐⢀⠂⠄⡁⢂⠡⠈⠄⡉⢉⠩⢉⠛⡉⠉⠍⡉⠠⢀⠡⠐⡀⢂⠁⢂⠁⠂⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠌⡀
⢄⡁⠂⠄⡁⠂⠄⠡⢈⠐⠠⠈⠄⡁⠂⠌⠠⢁⠂⡐⠠⢈⠐⡀⠂⠄⡁⢂⠰⢀⠂⠄⠂⠄⡁⠂⠄⡁⠂⠄⠡⠐⠠⠈⠄⡈⠌⠠⠁⠌⠠⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⠠⢁⠂⠄
      """)

print("""
      [+]Guia de uso para este script:
        - Ingrese el tipo de hash a auditar.
        - Ingrese el hash a auditar.
        - Ingrese la dirección del diccionario de contraseñas en formato unix, por ejemplo: /usr/share/wordlists/rockyou.txt

      """)

time.sleep(3)

print("""
    --Entre la lista de los hash admitidos.
      [+]sha1
      [+]sha224
      [+]sha256
      [+]sha384
      [+]sha512
      [+]sha3_224
      [+]sha3_256
      [+]sha3_384
      [+]sha3_512
      [+]blake2b
      [+]blake2s
      [+]md5
      

      """)

#Se le pide al usuario el tipo de hash
tipo_hash = input("[+]Ingresa el tipo de hash a aplicar fuerza bruta: ")

hashes = {
        'sha1':hashlib.sha1,
        'sha224':hashlib.sha224,
        'sha256':hashlib.sha256,
        'sha384':hashlib.sha384,
        'sha512':hashlib.sha512,
        'sha3_224':hashlib.sha3_224,
        'sha3_256':hashlib.sha3_256,
        'sha3_384':hashlib.sha3_384,
        'sha3_512':hashlib.sha3_512,
        #'shake_128':hashlib.shake_128,
        #'shake_256':hashlib.shake_256,
        'blake2b':hashlib.blake2b,
        'blake2s':hashlib.blake2s,
        'md5':hashlib.md5
        }
try:
    hash_name = hashes[tipo_hash.lower()]
except KeyError:
    print("[+]El tipo de hash no existe")
    exit()


#Main del programa y donde se hace la fuerza bruta
def brute_force():
    #Se le pide al usuario el hash
    hash = input("[+]Ingresa el hash: ")
    
    #Pedimos al usuario la dirección del wordlist para realizar la fuerza bruta 
    diccionario = input("[+]Ingresa la dirección tipo unix donde se encuentra el diccionario: ")
    #Se abre el diccionario en modo lectura
    with open(diccionario,"r") as wordlist:

        #Se itera sobre wordlist para hacer la fuerza bruta
        for word in wordlist.readlines(): #Volvemos cada linea una lista de cadenas
            word = word.strip() #Elimina espcaios y salto de linea 
            crypyted_password = hash_name(word.encode()).hexdigest() #Aquie se esta encritpando la palabra que se almacena en word 

            if hash == crypyted_password: #Realzia la comparacion de el hash que se pasa y el que se encripta en el diccionario
                print("[+]Password found: " + word) #En caso de ser correcat imprime la contraseña 
                break #Y se detiene
            else:
                print("[+]Incorrect password: " + word)#En caso contrario imprime la contraseña incorrecta probada

brute_force()



