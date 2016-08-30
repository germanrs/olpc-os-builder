# Copyright (C) 2015 One Laptop per Child
# Licensed under the terms of the GNU GPL v2 or later; see COPYING for details.
import ooblib
import urllib
import urlparse

baseurl = ooblib.read_config('sugar_activity_group', 'url')
vmaj = int(ooblib.read_config('global', 'olpc_version_major'))
vmin = int(ooblib.read_config('global', 'olpc_version_minor'))
vrel = int(ooblib.read_config('global', 'olpc_version_release'))
suffix = "%d.%d.%d" % (vmaj, vmin, vrel)
grpurl = urlparse.urljoin(baseurl + "/", urllib.quote(suffix))

print "echo generated by kspost.60.activities.py"
print "cat >$INSTALL_ROOT/usr/share/glib-2.0/schemas/sugar_activity_group.oob.gschema.override <<EOF"
print "[org.sugarlabs.update]"
print "backend='microformat.MicroformatUpdater'"
print "microformat-update-url='%s'" % grpurl
print "EOF"
print "/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas"