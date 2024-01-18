"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Polak
email: martin.polak@embedit.cz
discord: martin_24338
"""
import os
from task_template import TEXTS

if os.name == 'nt': 
    _ = os.system('cls')
else:  
    _ = os.system('clear')


uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

hvezda = "*"
pomlcka= "-"

def kontrola_udaju():
    # implementujte funkci pro kontrolu uživatelských dat
    while True:
        jmeno_uzivatele = input("Username: ").lower()
        heslo_uzivatele = input("Password: ")

        if  uzivatele.get(jmeno_uzivatele) and uzivatele[jmeno_uzivatele] == heslo_uzivatele:
            return True , jmeno_uzivatele #tuple vraci kontrolu a jmeno uzivate pro osloveni
        else:
            print("Your username or password is incorrect, try again")

# Volani funkce pro kontrolu udaju
result = kontrola_udaju()
if result[0]:
    print("Welcome to the app, ",result[1])
    print(pomlcka*30)
else:
    print("Login failed")

def check_amount_of_text():
    x=0
    for i in enumerate(TEXTS):
        if i:
            x+=1
    return x

#Vyber textu       
print("\n")
print (f'We have {check_amount_of_text()} text for choose, see below')
for i,text in enumerate(TEXTS):
    print(f'Text number {i+1}:\n {text}')
    print("\n")

while True:
 choice = int(input('\nChoose the number of the text you want to check: '))
 if not choice.isdigit() or int(choice) > len(TEXTS) or int(choice) <= 0:
            print('Wrong number! Try again.\n')
 else :
     print("Let's check text")
     print(pomlcka*30)
     break


        
print("\n")
  
choice = choice -1
split_text = TEXTS[choice].split()
pocet_slov=len(split_text)

title_case = 0
alpha = ([chr(i) for i in range(ord('A'), ord('Z')+1)])
for i in split_text:
   if (i[0] in alpha) and (i[1] not in alpha) :
      
      title_case +=1

uppercase_words = 0
lowercase_words = 0
digitcase_words = 0
digitcase_sum=0
lengt_longest_word=0

#analyza slov
for x in split_text:
    if x.isupper():
      uppercase_words+=1
    if x.islower():
      lowercase_words+=1
    if x.isdigit():
      digitcase_words+=1  
    if x.isdigit():
      digitcase_sum=digitcase_sum+int(x)
    if lengt_longest_word <= len(x):
      lengt_longest_word=len(x)
      
print('There are',pocet_slov,'words in the selected text.')
print('There are',title_case,'titlecase words.')
print('There are',uppercase_words,'uppercase words.')
print('There are',lowercase_words,'lowercase words.')
print('There are',digitcase_words,'numeric strings.')
print('The sum of all the numbers ',digitcase_sum)
print(sep="\n")


vycistena_slova = []
for x in split_text:
    ciste_slovo= x.strip(".,:,! ")
    vycistena_slova.append(ciste_slovo.lower())
delka_slov = {i: 0 for i in range(lengt_longest_word)}
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



