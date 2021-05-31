import time
import platform
import os

rojo = '\033[31m'
normal = '\033[39m'

print(normal+"")

respuesta1 = "1"
respuesta2 = "2"

clear

time.sleep(1)

print (rojo+"               ,;;;,   ,;;;,                             ")
time.sleep(1)
print (rojo+"              ;;;;;;;,;;;;;;;                            ")
time.sleep(1)
print (rojo+"     .:::.   .::::;;;;;;;;;;;                            ")
time.sleep(1)
print (rojo+"    :::::::.:::::::;;;;;;;;;'                            ")
time.sleep(1)
print (rojo+"    :::::::::::::::;;;;;;;'          by: Sherlock           ")
time.sleep(1)
print (rojo+"    ':::::::::::::';;;;;'                                ")
time.sleep(1)
print (rojo+"      ':::::::::'   ';'                                  ")
time.sleep(1)
print (rojo+"        ':::::'                                          ")
time.sleep(1)
print (rojo+"          ':'                                            ")
time.sleep(1)


print(normal+"")
nombre = input("Cual es tu nombre: ")
print(f"Hola {nombre}")

print("Queria preguntarte si... ¿Querias ser mi novia? :3 ")
print("1. Si <3")
print("2. No :(")
print("")
respuesta = input()

if (respuesta == respuesta1):
 print("")
 print("")

 print(f"Sabia que si querias serlo, te amo {nombre}")
 time.sleep(5)
 exit



if (respuesta == "2"):
 print("")
 print("")

 print("Yo solo queria hacerte feliz, espero encuentres a alguien que te ame y te valore mucho :( ")
 time.sleep(3)
 exit
