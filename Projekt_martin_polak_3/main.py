"""
projekt_3.py: treti projekt do Engeto Online Python Akademie

author: Martin Polak
email: martin.polak@gembedit.cz
discord: martin_24338
"""
import random
import os
import time

#vycisteni obrazovky
if os.name == 'nt': 
   os.system('cls')
else:  
   os.system('clear')



if __name__  == "__main__":
    text="kurva"

    muj_soubor =open("requirement.txt", mode="r",encoding='UTF-8')
   # muj_soubor.write(text + "\n") # zapis do souboru
    print(muj_soubor.read()) # cteni z souboru
    print(muj_soubor.tell())
    print(muj_soubor.seek(0)) #posunuti kurzoru na zacatek
    muj_soubor.close
    print(type(muj_soubor))

# nacitani obsahu souboru
with open ("requirement.txt","r") as f:
  #  read - precte cely soubor jako jeden string_
  #  readline - precte pouze prvni radek jako string
  #  readlines - precte cely soubor jako list (co radek to udaj)
    requirements=f.readlines()
print(requirements)

with open("requirement.txt",mode="r") as novy_file:
    with open("novy_cpy",mode="w") as novy_copy:
        novy_copy.write("First line \n")
        content = novy_file.read()
        novy_copy.write(content)
                

import os
os.listdir(os.getcwd())
#os.listdir ("/home/martinpolak atd cesta ke slozce") neco jako dir

soubory = os.listdir()
for soubor in soubory:
    print(soubor)

    os.path.isfile("novy.txt")
    >> True

os.path.isdir("solution")
>>False

if os.path.isfile("novy.txt"):
    with open("novy.txt") as f:
        print(f.read())


os.sep

f"uzivatel{os.sep)projekty"

"C:"+ os.sep + "uzivatel"

os.path.join("polak","Documents","Programovani")


os.getcwd()


#modul pathlib
from pathlib import Path

path = Path(".")
type(path), path

dirs = [x for x in path.iterdir()]

