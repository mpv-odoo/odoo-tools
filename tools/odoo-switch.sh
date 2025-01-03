#!/usr/bin/env bash

odoo_src="${ODOO_SRC}/odoo/"
enterprise_addons_src="${ODOO_SRC}/enterprise/"

odoo_version=$1

if [ "$odoo_version" = "18" ] || [ "$odoo_version" = "17" ] ||  [ "$odoo_version" = "16" ] || [ "$odoo_version" = "15" ] || [ "$odoo_version" = "14" ] || [ "$odoo_version" = "13" ] || [ "$odoo_version" = "12" ] || [ "$odoo_version" = "11" ]
then
    git_version="${odoo_version:1}"

    # Switch venvs to be the correct version
    pyenv activate $odoo_version

    # Switch odoo git to correct branch
    cd $odoo_src && git stash && git checkout ${odoo_version}.0 && git pull
    cd -

    # Switch enterprise addons to correct branch
    cd $enterprise_addons_src && git stash && git checkout ${odoo_version}.0 && git pull
    cd -

    echo "Successfully switched to version ${odoo_version}.0 of Odoo"
  
else 
      echo 'invalid version number, exiting'
fi