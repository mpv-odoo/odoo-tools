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

odoo_addon_name = sys.argv[2]

############################
##### Settings Parsing #####
############################
settings_f = open('settings.json')
settings = json.load(settings_f)


############################
####### Folder Init ########
############################
cwd = os.getcwd()
if os.path.exists(cwd + '/' + odoo_addon_name):
   print('Skipping creation of project directory as it already exists')
else:
   os.mkdir(f'{cwd}/{odoo_addon_name}')


# Make addons folder
if os.path.exists(cwd + '/' + odoo_addon_name + '/addons'):
   print('Skipping creating directory as it seems to exist already')
else: 
   os.mkdir(f'{cwd}/{odoo_addon_name}/addons')



# Create symlink with odoo source
subprocess.run(['ln', '-s', {settings['odoo_src']}, 'odoo'])

# Create symlink with enterprise source
subprocess.run(['ln', '-s', {settings['enterprise_src']}, 'enterprise'])

############################
###### Database Init #######
############################


''' 
Create dictionary of random
words to name the database
docker
'''
dict_len = 1000

# Create a dictionary with 1000 random words
rand_words = subprocess.run(['head', '-n', str(dict_len), '/usr/share/dict/words'], stdout=subprocess.PIPE).stdout.decode("utf-8").split()

'''
   @db_name is going to be the string that we will
   name both our odooo and database container
'''
db_name = (rand_words[randrange(dict_len)] + '-' + rand_words[randrange(dict_len)]).lower()

print(f'Generated Container Name: {db_name}')



'''
Random port must be > 1024, since
lower port numbers require sudo 
priviledge
'''
db_port = randrange(1024, 10000)
db_init = False


# Create the database container and print its id
print('Database Container ID: ')
db_exit_code = subprocess.run([
   f'docker', f'run',
   f'--name={db_name}-db',
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

