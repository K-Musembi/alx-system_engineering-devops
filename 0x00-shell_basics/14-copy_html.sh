#!/bin/sh
find . -maxdepth 1 -type f -name '*.html' -exec cp -u -n {} ../ \;
