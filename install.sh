#!/bin/bash

# テキストカラー
function green  { echo -e "\e[32m$*\e[m"; }
function red { echo -e "\e[31m$*\e[m"; }
function yellow { echo -e "\e[33m$*\e[m"; }

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v gnow`

if [ ${CMD_EXIST} ]; then
    red "'gnow' command already exist."
    exit 0
fi

if [ -e "${DIR}/bin/gnow" ]; then
    git config core.filemode false
    sudo ln -si ${DIR}/bin/gnow /usr/local/bin
    sudo chmod 777 ${DIR}/bin/gnow
    CMD_EXIST=`command -v gnow`
    if [ ${CMD_EXIST} ]; then
        green "Create 'gnow' command."
    else
        red "'Failed create 'gnow' command."
    fi
else
    red "'gnow' file not found."
fi

exit 0
