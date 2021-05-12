#!/bin/zsh

# Command to run: `source switch-odoo.sh <version number>
# Ex: `source switch-odoo.sh 12`


venvs='/Users/martin/Documents/GitHub/Work/src/odoo-venvs'
odoo_src='/Users/martin/Documents/GitHub/Work/src/odoo/'
enterprise_addons_src='/Users/martin/Documents/GitHub/Work/src/enterprise/'


odoo_version=$1

if [ $odoo_version -ne 14 ] && [ $odoo_version -ne 13 ] && [ $odoo_version -ne 12 ] && [ $odoo_version -ne 11 ]
then
    echo 'invalid version number, exitting'
else 
    # Switch venvs to be the correct version
    source "${venvs}/odoo-${odoo_version}/bin/activate"

    # Switch odoo git to correct branch
    cd $odoo_src && git checkout ${odoo_version}.0 && git pull
    cd -

    # Switch enterprise addons to correct branch
    cd $enterprise_addons_src && git checkout ${odoo_version}.0 && git pull
    cd -
fi



echo $odoo_version
