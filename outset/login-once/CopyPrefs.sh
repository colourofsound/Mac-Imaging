#!/bin/bash

# Copy Preferences from /usr/local/preferences to ~/Library/Preferences

chmod -R 755 /usr/local/Preferences

chown -R root:wheel /usr/local/Preferences

cp -r /usr/local/Preferences/* $HOME/Library/Preferences

# Use docklib to apply custom Dock layout

chmod -R 755 /usr/local/docklib

chown -R root:wheel /usr/local/docklib

python /usr/local/docklib/lab-dock.py