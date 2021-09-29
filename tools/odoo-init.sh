#!/bin/zsh


############################
###### SETTINGS INIT #######
############################

db_password=c0cac0la
db_username=odoo
############################
####### ARGS PARSING #######
############################
if [[ $# -eq 0 ]] ; then
    echo 'Need git url as argument'
    exit 1
fi

# Input should be the github url
git_url=$1
git_repo_user=$(echo $git_url | sed 's/.*.com://' | sed 's/\/.*//')
folder_name=$(echo "$git_url" | sed 's:.*/::' | sed 's/\.git.*//')
git_repo="${git_repo_user}/${folder_name}.git"
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
###### GIT FOLDER INIT #####
############################
git clone git@github-odoo:/${git_repo}
touch ${folder_name}/odoo.conf




# # Export the odoo conf file pwd
# export ODOO_CONF=$(pwd)/${folder_name}/odoo.conf

# Create the odoo.conf file
echo "[options] 
db_host = localhost
db_port = ${db_port}
db_user = ${db_username}
db_password = ${db_password}
db_name = postgres
addons_path = addons,../enterprise,$(pwd)/${folder_name}/" > ${folder_name}/odoo.conf
