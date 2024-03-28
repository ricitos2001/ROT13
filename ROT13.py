# -*- coding: utf-8 -*-
#! NO FUNCIONA CORRECTAMENTE

import os
import sys

def checkear_version_de_python():
    version_requerida = [(3, 10), (3, 11), (3, 12)]
    version_instalada = sys.version_info[:2]
    if version_instalada in version_requerida:
        verificacion="version de python: "+str(version_instalada)+"\nla version de python instalada es compatible."
        print(verificacion)
        os.system("pause")
        borrar_consola()
    else:
        verificacion="la version de python instalada es compatible\nes necesario tener instalado Python3.10, 3.11, o 3.12"
        print(verificacion)

def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def encriptar_mensaje(abecedario,rot13,mensaje):
    procesoencripcion=dict(zip(abecedario+rot13,rot13+abecedario))
    encripcion=''.join(procesoencripcion.get(i, i) for i in mensaje).lower()
    return encripcion

def desencriptar_mensaje(abecedario,rot13,mensaje):
    procesodesencripcion=dict(zip(rot13+abecedario,abecedario+rot13))
    desencripcion=''.join(procesodesencripcion.get(i, i) for i in mensaje).lower()
    return desencripcion

if __name__=="__main__":
    borrar_consola()
    checkear_version_de_python()
    abecedario='abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    rot13='nñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklm'
    error="solo esta permitido introducir 1, 2 o 3\n"
    while error:
        try:
            borrar_consola()
            menu="---------------ROT13!---------------\n\topcion 1: cifrado\n\topcion 2: descifrado\n\topcion 3: salir del programa\n---------------------------------------"
            print (menu)
            opcion=int(input("elige una opcion: "))
            if opcion==1:
                mensaje=str(input("introduce una frase: ")).lower()
                mensajeencriptado=encriptar_mensaje(abecedario,rot13,mensaje)
                print(mensajeencriptado)
            elif opcion==2:
                mensaje=str(input("introduce una frase: ")).lower()
                mensajedesencriptado=desencriptar_mensaje(abecedario,rot13,mensaje)
                print(mensajedesencriptado)
            elif opcion==3:
                mensaje="que tengas un buen dia"
                print(mensaje)
                break
            else:
                raise ValueError ("opcion invalida. intentalo de nuevo: ")
        except ValueError:
            print("opcion invalida. intentalo de nuevo: ")