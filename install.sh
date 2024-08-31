#!/usr/bin/env bash

if [[ -f "./build" ]]; then
    rm -rf ./build
fi

if [[ -f "./dist/utilitiestool" ]]; then
    rm -rf ./dist/utilitiestool
fi
.venv/bin/pyinstaller -D -F -n utilitiestool -c main.py --key TdQeHy_37dpg%erN7
if [[ -f "/usr/local/bin/utilitiestool" ]]; then
    rm -rf /usr/local/bin/utilitiestool
fi
cp dist/utilitiestool /usr/local/bin/utilitiestool
if [[ -f "/usr/local/bin/utilitiestool" ]]; then
    chmod 755 /usr/local/bin/utilitiestool
fi
