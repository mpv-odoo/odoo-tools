#!/bin/zsh

# Command to run: `source switch-odoo.sh <version number>
# Ex: `source switch-odoo.sh 12`


venvs="${ODOO_SRC}/odoo-venvs"
odoo_src="${ODOO_SRC}/odoo/"
enterprise_addons_src="${ODOO_SRC}/enterprise/"


odoo_version=$1

if [ "$odoo_version" -eq "14" ] || [ "$odoo_version" -eq "13" ] || [ "$odoo_version" -eq "12" ] || [ "$odoo_version" -eq "11" ]
then
    # Switch venvs to be the correct version
    pyenv activate $odoo_version

    # Switch odoo git to correct branch
    cd $odoo_src && git checkout ${odoo_version}.0 && git pull
    cd -

    # Switch enterprise addons to correct branch
    cd $enterprise_addons_src && git checkout ${odoo_version}.0 && git pull
    cd -

    echo "Successfully switched to version ${odoo_version}.0 of Odoo"
  
else 
      echo 'invalid version number, exitting'
fi