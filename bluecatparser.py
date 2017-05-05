#  Brandon Smith, 2017.5.5 v1.1 - bluecatparser.py
#  Tool for converting named.conf files.
#  To be used along with dns-comp-ms-isc.exe to test deployed DNS infrastructure
#  DNS DBs should be in the ./active/ folder. Creates a .conf file relative to the Views in BlueCat
#
#  Updated to merge .conf instead of the .db files.
#
import re
from shutil import copyfileobj

view = r'view \"(.*)\"'
zone = r'.*zone:\s(.*\b|\.)\s'
id = r'.*active\/(.*)\.conf.*'
reglist = (view, zone, id)

srcpath = "./active/"

with open("./named.conf", "r") as conf_file:
    for line in conf_file.readlines():
        if re.match(view, line):
            dnsview = re.match(view, line).group(1)
        if re.match(zone, line):
            dnszone = re.match(zone, line).group(1)
        if re.match(id, line):
            dnsid = re.match(id, line).group(1)
            destfile = open("./%s.conf" % (dnsview), 'a')
            try:
                copyfileobj(open("%s%s.conf" % (srcpath, dnsid), 'r'), destfile)
            except:
                print("error copying %s @%s - Possible forwarder" % (dnszone, dnsid))
            destfile.close()
