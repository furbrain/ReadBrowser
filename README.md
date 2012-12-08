ReadBrowser
===========

A very simple clinical system and associated read code browser with intelligent search

You will need wxPython, django and postgres installed. Create a postgres database called EHR, then run from the root directory of
the archive run:

./manage.py syncdb
##FIXME load readcodes.json via psql
./manage.py loaddata test_data.json
./manage.py wxrun problems

