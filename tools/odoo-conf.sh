#!/usr/bin/env bash
if [ ! -f "${ODOO_SRC}/odoo-sample.conf" ]; then
    echo "${ODOO_SRC}/odoo.conf does not exist"
    exit 1
fi

#PWD = $(pwd)
envsubst < ${ODOO_SRC}/odoo-sample.conf > odoo.conf