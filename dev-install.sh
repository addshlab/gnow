#!/bin/bash

# テキストカラー
function green  { echo -e "\e[32m$*\e[m"; }
function red { echo -e "\e[31m$*\e[m"; }
function yellow { echo -e "\e[33m$*\e[m"; }

DIR=$(cd $(dirname $0); pwd)
APP=gnow2
CMD_EXIST=`command -v ${APP}`

if [ ${CMD_EXIST} ]; then
    red "'${APP}' command already exist."
    exit 0
fi

if [ -e "${DIR}/bin/gnow.py" ]; then
    git config core.filemode false
    sudo ln -si ${DIR}/bin/gnow.py /usr/local/bin/${APP}
    sudo chmod 777 ${DIR}/bin/gnow.py
    CMD_EXIST=`command -v ${APP}`
    if [ ${CMD_EXIST} ]; then
        green "Create ${APP} command."
    else
        red "'Failed create ${APP} command."
    fi
else
    red "'gnow.py' file not found."
fi

exit 0
