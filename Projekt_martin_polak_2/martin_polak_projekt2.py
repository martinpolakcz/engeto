"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Martin Polak
email: martin.polak@gembedit.cz
discord: martin_24338
"""
import random
import os


if os.name == 'nt': 
    _ = os.system('cls')
else:  
    _ = os.system('clear')

pomlcky = '-'
print("Hi there!")
print(pomlcky*20)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(pomlcky*20)

def generate_random_number():
    unique = False
    while not unique:
        num = random.randint(1000, 9999)
        if num not in previously_generated:
            previously_generated.add(num)
            unique = True
    return num

previously_generated = set()
random_number = generate_random_number()
#print(random_number)



def check_tip(tip_user,generated_number):
   tip_user = list(map(int, str(tip_user)))
   generated_number = list(map(int, str(generated_number)))
   #print(tip_user)
   #print(generated_number)
   

   bulls = 0
   cows = 0
   for i in range(len(tip_user)):
    if tip_user[i] == generated_number[i]: 
       # bulls pokud je cislo na stejnem miste
       bulls += 1

    if tip_user[i] in generated_number:
        # cows pokud je cislo v tomto polozeni ale ne na ste
       cows += 1

            
   print(f'Bulls:{bulls}')
   print(f'Cows:{cows}') 
   return bulls    

def validation_number():
   validation_ok = False
   while validation_ok == False:
      choose_number= input("Enter a number: ")
      list_number = list( str(choose_number))
      if len(choose_number) <4 : 
       print(f'Your number {choose_number} is less digits than 4')
       validation_ok = False
      elif(len(choose_number) >4):
         print('Number can not be longer than 4 digits')
         validation_ok = False
      elif not (choose_number.isdigit()):
         print("Your input doesn't include only digits")
         validation_ok = False
      elif(list_number[0]=='0'):
         print('Number start with 0 digits, which is incorrect')
         validation_ok = False

      else:
         print("Your input is correct, welcome in the game")
         validation_ok = True
         return choose_number
      

value=0
attempts =0
while value !=4:   
   pomlcky = '-'
   choose_number=validation_number()
   print(choose_number)
   print(pomlcky*20)
   value=check_tip(choose_number,random_number)
  # print(f'tady je hodnota:{value}')
   if value != 4:
      print("Try again")
      attempts +=1
      print(pomlcky*20)
   else:
      print("You won! Congratulations!")
      print(f'Number of attempts: {attempts}')
