#!/bin/bash

git fetch
git reset --hard origin/master

# Now replace the static_settings file with the locally
# saved prod version
cp ../static_settings.py .

sudo service uwsgi reload
