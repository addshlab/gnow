#!/bin/bash

# テキストカラー
function green  { echo -e "\e[32m$*\e[m"; }
function red { echo -e "\e[31m$*\e[m"; }
function yellow { echo -e "\e[33m$*\e[m"; }

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v gnow`

sudo chmod 777 ${DIR}/bin/gnow

if [ ${CMD_EXIST} ]; then
    sudo unlink /usr/local/bin/gnow
    sudo chmod 646 ${DIR}/bin/gnow
    green "Delete 'gnow' command."
else
    red "'gnow' command not found."
fi

exit 0
