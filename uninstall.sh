#!/bin/bash

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v gnow`

sudo chmod 777 ${DIR}/gnow

if [ ${CMD_EXIST} ]; then
    sudo unlink /usr/local/bin/gnow
    sudo chmod 646 ${DIR}/bin/gnow
    echo "delete 'gnow' command."
else
    echo "'gnow' command not found."
fi

exit 0
