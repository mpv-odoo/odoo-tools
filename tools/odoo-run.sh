#!/usr/bin/env bash

echo $@

if [ "$1" = "default" ]
then
    shift
    echo $ODOO_CONF
    python3 -m debugpy --listen 5678 "${ODOO_SRC}/odoo/odoo-bin" --config=$ODOO_CONF $@
else
    ODOO_CONF_ARG=$(realpath $1)
    shift
    echo $ODOO_CONF_ARG
    python3 -m debugpy --listen 5678 "${ODOO_SRC}/odoo/odoo-bin" --config=$ODOO_CONF_ARG $@
fi



