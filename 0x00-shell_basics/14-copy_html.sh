#!/bin/sh
find . -name "*.html" -exec sh -c 'cp -u "$0" "../$(basename "$0")"' {} \;
