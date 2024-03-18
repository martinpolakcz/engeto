#pip install setuptools
#pip install requests

import pip
import os
import requests
import sys
import setuptools
import pkg_resources
import  subprocess
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd 

#procisteni terminalu
if os.name == 'nt': 
   os.system('cls')
else:  
   os.system('clear')


#generovani pozadavku do souboru
def generate_requirements():
  with open ("requirements.txt","w") as f:

#vytahne seznam  z PyPi a ulozi ho do txt
    installed_packages = [dist.project_name for dist in pkg_resources.working_set]
    installed_packages_list = [f"{dist}=={pkg_resources.get_distribution(dist).version}" for dist in installed_packages]
    #print("Installed packages: ")
    f.write("\n")
    #print(installed_packages_list)
    #f.write("Installed packages: \n")
    f.write("\n".join(installed_packages_list))
    #f.write("\n")
    f.close()
    

   
def get_url_file_name():

  url = str(sys.argv[1])
  file_name = str(sys.argv[2])
  print("URL adresa zadana uživatelem je: ", url)
  try:
    response_server=requests.get(url)
    if response_server.status_code != 200:
         print("Sorry, the URL address ", url, " is not available!")
         sys.exit()
  except requests.exceptions.RequestException as e:
     print('Sorry, the URL address ', url, ' is not available!')
     sys.exit()
 
  print("Jméno souboru pro uložení výpisů je: ", file_name)
  return url, file_name

global obec_id

print("Program vypíše nainstalované balíčky a ukládá je do souboru.")





def write_to_file(url, filename):
   content = requests.get(url).text
   source_text = BeautifulSoup(content,'html.parser')
   with open(filename, 'w') as f:
      #f.write(content) 


#new
 
      number_v = source_text.find_all('td',attrs={"class": "cislo"})
      name_v = source_text.find_all('td',attrs={"class": "overflow_name"})

      data = {}
      data_all = []
      data_table_strany = []
      url_next1 = f"https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec={number_v[0].text.strip()}"
      content_name = requests.get(url_next1).text
      source_name = BeautifulSoup(content_name,'html.parser')
     # print(url_next1)
      
      #toto vytahne data pro hlavisku v tabulce
      voters_in_the_list_name = source_name.body.find(id='ps311_t1', class_='table').contents[1].contents[3].text
      #print(voters_in_the_list_name)

      letter_covers_name = source_name.body.find(id='ps311_t1', class_='table').contents[1].contents[5].text
      #print(letter_covers_name)

      valid_vote_name = source_name.body.find(id='ps311_t1', class_='table').contents[1].contents[11].text
      #print(valid_vote_name)

      for td in source_name.find_all('td', class_='overflow_name', headers=['t1sa1 t1sb2']):
        data_table_strany.append(td.text)
      for td in source_name.find_all('td', class_='overflow_name', headers=['t2sa1 t2sb2']):
        data_table_strany.append(td.text)
      #print(data_table_strany)

      data_all_name=['kód_obce','název_obce',voters_in_the_list_name,letter_covers_name,valid_vote_name,data_table_strany]
      data_all_name[-1] = ','.join(map(str, data_all_name[-1]))
      data_string_name = ','.join(map(str, data_all_name))
      #data_string_name = data_string_name.replace(',', ', ')
      f.write(data_string_name + '\n')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

      for number, name in zip(number_v, name_v):
         data_table = []
         data[number.text.strip()] = name.text.strip()
        # print(data)



         url_next = f"https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec={number.text.strip()}"
         #generovani processu do terminalu
         print(f"Processing: {number.text} : {name.text}")
     #    print(url_next)

         content_village = requests.get(url_next).text
         source_text_village = BeautifulSoup(content_village,'html.parser')
      #   print(f'toto je source_text_village {source_text_village}')

         voters_in_the_list = source_text_village.body.find( id='ps311_t1', class_='table').contents[5].contents[7].text
         #print("volici v seznamu: ",voters_in_the_list)
         letter_covers = source_text_village.body.find( id='ps311_t1', class_='table').contents[5].contents[9].text
         #print("vydane obalky: ",letter_covers)
         valid_vote = source_text_village.body.find( id='ps311_t1', class_='table').contents[5].contents[15].text
         #print("platne hlasy: ",valid_vote)

         for td in source_text_village.find_all('td', class_='cislo', headers=['t1sa2 t1sb3']):
           data_table.append(td.text)
         for td in source_text_village.find_all('td', class_='cislo', headers=['t2sa2 t2sb3']):
           data_table.append(td.text)

        #vlozeni vsech dat do data all pro ulozeni
         data_all=[number.text.strip(),name.text.strip(),voters_in_the_list,letter_covers,valid_vote,data_table]
         data_all[-1] = ','.join(map(str, data_all[-1]))

         data_string = ','.join(map(str, data_all))
         data_string = data_string.replace('\xa0', '')

         f.write(data_string + '\n')
         





if __name__ == '__main__':
   generate_requirements()
   url, file_name = get_url_file_name()
   write_to_file(url, file_name)





