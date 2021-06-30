# Have flag for enabling debugging
# open up odoo in browser if possible
# globally run odoo command from anywhere


# Check if odoo.conf exists in parent directory
# If it does, then run with it
# If it doesn't, 

echo $@


ODOO_CONF=$(realpath $1)
shift

echo $ODOO_CONF

if test -f "$ODOO_CONF"; then
    python3 -m debugpy --listen 5678 "${ODOO_SRC}/odoo/odoo-bin" --config=$ODOO_CONF $@
fi