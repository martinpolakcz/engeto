"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Polak
email: martin.polak@gembedit.cz
discord: martin_24338
"""
from task_template import TEXTS



hvezda = "*"
pomlcka= "-"

def kontrola_udaju(jmeno_uzivatele, heslo_uzivatele):
# implementujte funkci pro kontrolu uživatelských dat
    uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

    if jmeno_uzivatele in uzivatele and uzivatele[jmeno_uzivatele] == heslo_uzivatele:
        return True
    else:
        return False

jmeno_uzivatele = input("zedej jmeno: ")
heslo_uzivatele = input("zadej heslo: ")

while not kontrola_udaju(jmeno_uzivatele, heslo_uzivatele):
         print("Nespravne jmeno nebo heslo. Zkus to znovu")
         jmeno_uzivatele = input("zedej jmeno: ")
         heslo_uzivatele = input("zadej heslo: ")

   



print("Prihlaseno!")


        



print("\n")
print ("We have 3 text for choose, see below")
for i,text in enumerate(TEXTS):
    print(f'Text number {i+1}:\n {text}')
    print("\n")
  
volba = int(input("Enter a number btw. 1 and 3 to select: "))
print("\n")
volba = volba -1
pocet_slov_split = TEXTS[volba].split()
pocet_slov=len(pocet_slov_split)

title_case = 0
alpha = ([chr(i) for i in range(ord('A'), ord('Z')+1)])
vyber=TEXTS[volba].split()
for i in vyber:
   if (i[0] in alpha) and (i[1] not in alpha) :
      
      title_case +=1

uppercase_words = 0
for x in vyber:
    if x.isupper():
      uppercase_words+=1


lowercase_words = 0
for x in vyber:
   if x.islower():
      lowercase_words+=1

   digitcase_words = 0
for x in vyber:
   if x.isdigit():
      digitcase_words+=1

digitcase_sum=0
for x in vyber:
   if x.isdigit():
      digitcase_sum=digitcase_sum+int(x)
      
print('There are',pocet_slov,'words in the selected text.')
print('There are',title_case,'titlecase words.')
print('There are',uppercase_words,'uppercase words.')
print('There are',lowercase_words,'lowercase words.')
print('There are',digitcase_words,'numeric strings.')
print('The sum of all the numbers ',digitcase_sum)
print(sep="\n")

vycistena_slova = []
for x in vyber:
    ciste_slovo= x.strip(".,:,! ")
    vycistena_slova.append(ciste_slovo.lower())

delka_slov = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
vyskyt_slov = {}
for x in vycistena_slova:
        vyskyt_slov[x] = len(x)
        y = vyskyt_slov[x]
        delka_slov[y]+=1

print(pomlcka*30)
print(f'{"LEN":<3}|{"OCCURENCES".center(21)}|NR.') 
print(pomlcka*30)
for vypis in delka_slov:
    print(f'{vypis: <3}|{hvezda*delka_slov[vypis] :<20} | {delka_slov[vypis]}',sep="\n")  



