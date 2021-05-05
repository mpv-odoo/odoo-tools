#!/usr/bin/env python3

import os
import subprocess
import sys
import json
from random import randrange

############################
####### Arg Parsing ########
############################
args = sys.argv

if len(sys.argv) < 3:
   print('Not enough args')
   exit()

odoo_version = int(sys.argv[1])

if odoo_version != 14 and odoo_version != 13 and odoo_version != 12:
   print('invalid odoo version')
   exit()

odoo_folder_name = sys.argv[2]

############################
##### Settings Parsing #####
############################
settings_f = open('settings.json')
settings = json.load(settings_f)


############################
####### Folder Init ########
############################
cwd = os.getcwd()
if os.path.exists(cwd + '/' + odoo_folder_name):
   print('Skipping creation of directory as it already exists')
else:
   os.mkdir(f'{cwd}/{odoo_folder_name}')


# Make addons folder
if os.path.exists(cwd + '/' + odoo_folder_name + '/addons'):
   print('Skipping creating directory')
else: 
   os.mkdir(f'{cwd}/{odoo_folder_name}/addons')

# Make addons folder
if os.path.exists(cwd + '/' + odoo_folder_name + '/config'):
   print('Skipping creating directory')
else: 
   os.mkdir(f'{cwd}/{odoo_folder_name}/config')



''' 
Length of the dictionary we
are going to make
'''
dict_len = 1000

# Create a dictionary with 1000 random words
rand_words = subprocess.run(['head', '-n', str(dict_len), '/usr/share/dict/words'], stdout=subprocess.PIPE).stdout.decode("utf-8").split()

'''
   @odoo_name is going to be the string that we will
   name both our odooo and database container
'''
odoo_name = (rand_words[randrange(dict_len)] + '-' + rand_words[randrange(dict_len)]).lower()

print(f'Generated Container Name: {odoo_name}')

############################
###### Database Init #######
############################

'''
Random port must be > 1024, since
lower port numbers require sudo 
priviledge
'''
db_port = randrange(1024, 10000)
db_init = False

#while not db_init:

# Create the database container and print its id
print('Database Container ID: ')
db_exit_code = subprocess.run([
   'docker', 'run',
   f'--name={odoo_name}-db',
   f'-p', f'{db_port}:5432',
   f'-d',
   f'-e', f'POSTGRES_PASSWORD={settings["db_password"]}',
   f'-e', f'POSTGRES_USER={settings["db_username"]}',
   f'-e', f'POSTGRES_DB=postgres',
   f'postgres'
])
print(db_exit_code)
print(type(db_exit_code))
if db_exit_code == 0:
   db_init = True



odoo_port = randrange(1024, 10000)


odoo_exit_code = subprocess.run([
   'docker', 'run',
   f'--name={odoo_name}',
   f'-p', f'{odoo_port}:8069',
   f'-d',
   f'-e', f'USER=odoo',
   f'-e', f'PASSWORD=c0cac0la',
   f'--link', f'{odoo_name}-db:db',
   f'-v', f'{cwd}/{odoo_folder_name}/config:/etc/odoo',
   f'-v', f'{cwd}/{odoo_folder_name}/addons:/mnt/extra-addons',
   f'odoo'
])