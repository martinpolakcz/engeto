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


lenght_pass = 4

#generovani nahodneho cisla s kontrolou na opakovani cisel
def generate_random_number():
   secret_number=[]
   num_list = [0,1,2,3,4,5,6,7,8,9]
   num_0 = random.sample(num_list[1:], 1)
   integer_value = int(str(num_0).strip('[]').replace(',', ''))
   secret_number.append(integer_value)
   num_list.remove(integer_value)

   num=dict()
   for i in  range(lenght_pass - 1):
      num[i] = random.sample(num_list, 1)
      integer_value = int(str(num[i]).strip('[]').replace(',', ''))
      secret_number.append(integer_value)
      num_list.remove(integer_value)
      
   secret_number = int(''.join(map(str, secret_number)))
   return str(secret_number)

#kontrola samotne hry
def check_tip(tip_user,generated_number):

   bulls = 0
   cows = 0
   for i in range(len(tip_user)):
    if tip_user[i] == generated_number[i]:
       # bulls pokud je cislo na stejnem miste a nebo je obsazen v cisle
       bulls += 1
       
    if  tip_user[i] in generated_number:
        # cows pokud je cislo aspon nekde v cisle na nejake pozici
       cows += 1
    

            

   return bulls  ,cows  

#kontrola validace hadaneho cisla
def validation_number(check_input):
      
      list_number = list( str(check_input))
      if not (check_input.isdigit()):
         print("Your input doesn't include only digits")
      elif len(check_input) <4 : 
       print(f'Your number {check_input} is less digits than 4')
      elif(list_number[0]=='0'):
         print('Number start with 0 digits, which is incorrect')
      elif(len(check_input) >4):
         print('Number can not be longer than 4 digits')
      else:
         print("Your input is correct, welcome in the game")
         print(pomlcky*20)
         return True

#zacatek programu Let's play
pomlcky = '-'
print("Hi there!")
print(pomlcky*20)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(pomlcky*20)

#generovani nahodneho cisla
random_number = generate_random_number()
#print(f'Generated number is: {random_number}')  #--jen pro testovani

bulls=0
attempts =0
#spusteni casovace pro "competition"
start_time = time.time()
while bulls !=4:  
   choose_number= input("Enter a number: ") 
   #validace vstupu pomoci funkce
   while  not validation_number(choose_number):
     choose_number= input("Please enter again a correct number: ")
   print(f'>>> {choose_number}')
   #kontrola TIPu
   bulls ,cows =check_tip(choose_number,random_number)
   print(f'Bulls:{bulls}')
   print(f'Cows:{cows}') 
  # value = bulls
   if bulls != 4:
      print("Try again")
      attempts +=1
      print(pomlcky*20)
   else:
      end_time = time.time()
      elapsed_time = round(end_time - start_time,2)
      print("You won! Congratulations!")
      print(f"Number of attempts: {attempts} and in time {elapsed_time} seconds")

