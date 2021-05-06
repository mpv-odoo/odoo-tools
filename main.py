#!/usr/bin/env python3

import os
import subprocess
import sys
import json
from random import randrange


############################
######### Settings #########
############################
ODOO_SRC = '/Users/martin/Documents/GitHub/Work/src/odoo'
ENTERPRISE_SRC = '/Users/martin/Documents/GitHub/Work/src/enterprise'
DB_USERNAME = 'odoo'
DB_PASSWORD = 'c0cac0la'



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
####### Folder Init ########
############################
cwd = os.getcwd()
if os.path.exists(cwd + '/' + odoo_addon_name):
   print('Skipping creation of project directory as it already exists')
else:
   print('Creating project directory')
   os.mkdir(f'{cwd}/{odoo_addon_name}')

# Make addons folder
if os.path.exists(cwd + '/' + odoo_addon_name + '/addons'):
   print('Skipping creating directory as it seems to exist already')
else:
   print('Creating addons directory')
   os.mkdir(f'{cwd}/{odoo_addon_name}/addons')

# Create symlink with odoo source
print('Creating a symlink with the odoo source folder')
subprocess.call(
   f'ln -s {ODOO_SRC} {odoo_addon_name}/odoo',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)
# Create symlink with enterprise source
print('Creating a symlink with the odoo enterprise source folder')
subprocess.call(
   f'ln -s {ENTERPRISE_SRC} {odoo_addon_name}/enterprise',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)



############################
####### Git Init ###########
############################

# Switch the odoo git to be the correct version
print(f'Changing odoo src branch to {odoo_version}.0')
subprocess.call(
   f'cd {odoo_addon_name}/odoo/ && git checkout {odoo_version}.0 && cd ..',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)
# Switch the enterprise git to be the correct version
print(f'Changing odoo enterprise src branch to {odoo_version}.0')
subprocess.call(
   f'cd {odoo_addon_name}/enterprise && git checkout {odoo_version}.0 & cd ..',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)



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
rand_words = subprocess.run(
   f'head -n {str(dict_len)} /usr/share/dict/words',
   stdout=subprocess.PIPE,
   shell=True
).stdout.decode("utf-8").split()

'''
   @db_name is going to be the string that we will
   name both our odooo and database container
'''
db_name = (
   rand_words[randrange(dict_len)] + 
   '-' + 
   rand_words[randrange(dict_len)]
).lower()

print(f'Generated Database Container Name: {db_name}')

'''
Random port must be > 1024, since
lower port numbers require sudo 
priviledge
'''
db_port = randrange(1024, 10000)
db_init = False


# # Create the database container and print its id
print('Starting Database Container')
subprocess.call([
   f'docker', f'run',
   f'--name={db_name}-db',
   f'-p', f'{db_port}:5432',
   f'-d',
   f'-e', f'POSTGRES_PASSWORD={DB_PASSWORD}',
   f'-e', f'POSTGRES_USER={DB_USERNAME}',
   f'-e', f'POSTGRES_DB=postgres',
   f'postgres'],
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)


############################
####### VSCode Init ########
############################
subprocess.call(
   f'code {odoo_addon_name}',
   shell=True
)
