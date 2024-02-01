"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

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

#generovani nahodneho cisla s kontrolou na opakovani cisel
def generate_random_number():
    unique = False
    previously_generated = set()
    while not unique:
        num = random.randint(1000, 9999)
        num_duplicity = 0
        if len(previously_generated) == 0 or num not in previously_generated:
            previously_generated.add(num)
            check=str(num)
            for i in range(len(check)):
               for x in range(len(check)):
                  if i==x:
                     continue
                  elif check[i]==check[x]:
                      num_duplicity = 1
                      break
        if num_duplicity == 0 and previously_generated != num:
           previously_generated.add(num)
           unique =  True
        else:
           pass

    return num

#kontrola samotne hry
def check_tip(tip_user,generated_number):
   tip_user = list(map(int, str(tip_user)))
   generated_number = list(map(int, str(generated_number)))
   bulls = 0
   cows = 0
   for i in range(len(tip_user)):
    if (tip_user[i] == generated_number[i]) and (tip_user[i] in generated_number):
       # bulls pokud je cislo na stejnem miste a nebo je obsazen v cisle
       bulls += 1
       cows += 1

    elif (tip_user[i] != generated_number[i]) and (tip_user[i] in generated_number):
        # cows pokud je cislo aspon nekde v cisle na nejake pozici
       cows += 1
    continue

            
   print(f'Bulls:{bulls}')
   print(f'Cows:{cows}') 
   return bulls    

#kontrola validace hadaneho cisla
def validation_number():
   validation_ok = False
   while validation_ok == False:
      choose_number= input("Enter a number: ")
      list_number = list( str(choose_number))
      if not (choose_number.isdigit()):
         print("Your input doesn't include only digits")
         validation_ok = False
      elif len(choose_number) <4 : 
       print(f'Your number {choose_number} is less digits than 4')
       validation_ok = False
      elif(list_number[0]=='0'):
         print('Number start with 0 digits, which is incorrect')
         validation_ok = False
      elif(len(choose_number) >4):
         print('Number can not be longer than 4 digits')
         validation_ok = False
      else:
         print("Your input is correct, welcome in the game")
         print(pomlcky*20)
         validation_ok = True
         return choose_number

#zacatek programu
pomlcky = '-'
print("Hi there!")
print(pomlcky*20)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(pomlcky*20)

random_number = generate_random_number()
#print(random_number)  --jen pro testovani

value=0
attempts =0
start_time = time.time()
while value !=4:   
   choose_number=validation_number()
   print(f'>>> {choose_number}')
   
   value=check_tip(choose_number,random_number)
   if value != 4:
      print("Try again")
      attempts +=1
      print(pomlcky*20)
   else:
      end_time = time.time()
      elapsed_time = round(end_time - start_time,2)
      print("You won! Congratulations!")
      print(f"Number of attempts: {attempts} and in time {elapsed_time} seconds")
