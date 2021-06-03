#!/bin/bash

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v gnow`

if [ ${CMD_EXIST} ]; then
    echo "'gnow' command already exist."
    exit 0
fi

if [ -e "${DIR}/bin/gnow" ]; then
    git config core.filemode false
    sudo ln -si ${DIR}/bin/gnow /usr/local/bin
    sudo chmod 777 ${DIR}/bin/gnow
    CMD_EXIST=`command -v gnow`
    if [ ${CMD_EXIST} ]; then
        echo "create 'gnow' command."
    else
        echo "'failed create 'gnow' command."
    fi
else
    echo "'gnow' file not found."
fi

exit 0
