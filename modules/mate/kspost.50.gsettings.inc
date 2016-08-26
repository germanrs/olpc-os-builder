# enlarge cursor #12848
cat >/usr/share/glib-2.0/schemas/mate.oob.gschema.override <<EOF
[org.mate.peripherals-mouse]
cursor-size=48

# set font size to 7
[org.mate.interface]
font-name='Sans 7'

document-font-name='Sans 7'

monospace-font-name='Monospace 7'

[org.mate.Marco.general]
titlebar-font='Sans Bold 7'

[org.mate.caja.desktop]
font='Sans 7'

EOF
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas
