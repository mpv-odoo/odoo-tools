#!/usr/bin/env python3

import os
import subprocess
import sys
import argparse
from random import randrange


############################
######### Settings #########
############################
ODOO_SRC = '/Users/martin/Documents/GitHub/Work/src/odoo'
ENTERPRISE_SRC = '/Users/martin/Documents/GitHub/Work/src/enterprise'
DB_USERNAME = 'odoo'
DB_PASSWORD = ''



############################
####### Arg Parsing ########
############################
parser = argparse.ArgumentParser()

# Add Folder name as argument
parser.add_argument(
   'addon_name',
   type=str,
   help='The name for the project you wish to set up'
)
# Add Odoo version as argument
parser.add_argument(
   'odoo_version',
   type = int,
   help = 'Odoo version number you wish to set up a project for (11, 12, 13)'
)
# Add optional flag to also run a postgres docker
parser.add_argument(
   '-db',
   '--database',
   action='store_true',
   help = 'Add this flag if you do want to also create a postgres docker container'
)
# Add optional flag to open up vscode
parser.add_argument(
   '-vs',
   '--vscode',
   action='store_true',
   help = 'Add this flag if you want to also open up vscode in the new project directory'
)
args = parser.parse_args()



############################
####### Folder Init ########
############################
cwd = os.getcwd()
if os.path.exists(cwd + '/' + args.addon_name):
   print('Skipping creation of project directory as it already exists')
else:
   print('Creating project directory')
   os.mkdir(f'{cwd}/{args.addon_name}')

# Make addons folder
if os.path.exists(cwd + '/' + args.addon_name + '/addons'):
   print('Skipping creating directory as it seems to exist already')
else:
   print('Creating addons directory')
   os.mkdir(f'{cwd}/{args.addon_name}/addons')

# Create symlink with odoo source
print('Creating a symlink with the odoo source folder')
subprocess.call(
   f'ln -s {ODOO_SRC} {args.addon_name}/odoo',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)
# Create symlink with enterprise source
print('Creating a symlink with the odoo enterprise source folder')
subprocess.call(
   f'ln -s {ENTERPRISE_SRC} {args.addon_name}/enterprise',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)



############################
####### Git Init ###########
############################

# Switch the odoo git to be the correct version
print(f'Changing odoo src branch to {args.odoo_version}.0')
subprocess.call(
   f'cd {args.addon_name}/odoo/ && git checkout {args.odoo_version}.0 && cd ..',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)
# Switch the enterprise git to be the correct version
print(f'Changing odoo enterprise src branch to {args.odoo_version}.0')
subprocess.call(
   f'cd {args.addon_name}/enterprise && git checkout {args.odoo_version}.0 & cd ..',
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL,
   shell=True
)



############################
###### Database Init #######
############################

# # Create the database container and print its id
if args.database:
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
if args.vscode:
   subprocess.call(
      f'code {args.addon_name}',
      shell=True
   )
