#!/bin/zsh


############################
###### SETTINGS INIT #######
############################

db_password=c0cac0la
db_username=odoo
############################
######### DB INIT ##########
############################

# Generate random word to use for the database name
rand_word_1=$(shuf -n1 /usr/share/dict/words| cut -d$'\t' -f1)
rand_word_2=$(shuf -n1 /usr/share/dict/words| cut -d$'\t' -f1)
db_name=${rand_word_1}-${rand_word_2}

# Get random port number for the db
db_port=$((1024 + $RANDOM % 10000))

# Create the database docker
docker run --name=${db_name} -p ${db_port}:5432 -d -e POSTGRES_PASSWORD=${db_password} -e POSTGRES_USER=${db_username} -e POSTGRES_DB=postgres postgres


############################
####### FOLDER INIT ########
############################

# Create a root folder for the addon
addon_name=$1
mkdir $addon_name
mkdir ${addon_name}/addons
touch ${addon_name}/odoo.conf


# Export the odoo conf file pwd
export ODOO_CONF=$(pwd)/${addon_name}/odoo.conf

# Create the odoo.conf file
echo "[options] 
db_host = localhost
db_port = 5432
db_user = odoo db_password = c0cac0la
db_name = postgres
addons_path = addons,../enterprise,$(pwd)/addons" > ${addon_name}/odoo.conf
