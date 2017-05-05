# BlueCatParser

BlueCat stores their BIND named.conf in tiers. The main named.conf, then under /etc/active/ for the actual per zone config files.
Each zone file abstracted with a unique ID.

This is just the initial commit, open for suggestions. 

The script parses the named.conf file, identifies the view, zone name and ID, then builds a new VIEW.conf file per view.

Just need to make sure the the ./dbs/ and ./active/ directories are in the same location of the bluecarparser.py

