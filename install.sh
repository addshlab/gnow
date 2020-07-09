#!/bin/bash

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v cfn`

if [ ${CMD_EXIST} ]; then
    echo "'cfn' command already exist."
    exit 0
fi

if [ -e "${DIR}/bin/cfn" ]; then
    sudo ln -si ${DIR}/bin/cfn /usr/local/bin
    sudo chmod 777 ${DIR}/bin/cfn
    CMD_EXIST=`command -v cfn`
    if [ ${CMD_EXIST} ]; then
        echo "create 'cfn' command."
    else
        echo "'failed create 'cnf' command."
    fi
else
    echo "'cfn' file not found."
fi

exit 0
