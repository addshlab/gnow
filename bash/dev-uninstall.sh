#!/bin/bash

# テキストカラー
function green  { echo -e "\e[32m$*\e[m"; }
function red { echo -e "\e[31m$*\e[m"; }
function yellow { echo -e "\e[33m$*\e[m"; }

DIR=$(cd $(dirname $0); pwd)

APP=gnow
CMD_EXIST=`command -v ${APP}`

sudo chmod 777 ${DIR}/bin/gnow.py

if [ ${CMD_EXIST} ]; then
    sudo unlink /usr/local/bin/${APP}
    sudo chmod 646 ${DIR}/bin/gnow.py
    green "Delete '${APP}' command."
else
    red "'${APP}' command not found."
fi

exit 0
