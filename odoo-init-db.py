#!/usr/local/bin/python3

import os
import subprocess
import argparse
from dotenv import load_dotenv, dotenv_values

############################
####### Arg Parsing ########
############################
load_dotenv()
parser = argparse.ArgumentParser()

parser.add_argument(
    'db_name',
    type=str,
    help='The database name'
)
parser.add_argument(
    '-p',
    '--port',
    type=int,
    default=5432,
    help='Optional database port number (default is 5342)'
)
args = parser.parse_args()

print('Starting Database Container')
subprocess.call([
    f'docker run --name={args.db_name} \
    -p {args.port}:5432 \
    -e POSTGRES_PASSWORD={os.getenv("DB_PASSWORD")} \
    -e POSTGRES_USER={os.getenv("DB_USERNAME")} \
    -e POSTGRES_DB=postgres \
    -d \
    postgres'
],
    shell=True
)