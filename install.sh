#!/bin/zsh
BIN_FOLDER='/usr/local/bin/'
ZSHRC='/Users/martin/.zshrc'
ODOO_SRC='/Users/martin/Documents/Work/Source'

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Remove previous link (if exists) and make new symlink
rm -f /usr/local/bin/odoo-switch
ln -s $(pwd)/tools/odoo-switch.sh /usr/local/bin/odoo-switch


# Add the zsh shortcuts/vars to the .zshrc file
echo "

# Added by odoo-tools install script
export ODOO_SRC=$ODOO_SRC

function swodoo() {
    source odoo-switch $1
}

" >> $ZSHRC