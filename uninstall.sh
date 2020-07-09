#!/bin/bash

DIR=$(cd $(dirname $0); pwd)

CMD_EXIST=`command -v cfn`

if [ ${CMD_EXIST} ]; then
    sudo unlink /usr/local/bin/cfn
    sudo chmod 646 ${DIR}/bin/cfn
    echo "delete 'cfn' command."
else
    echo "'cfn' command not found."
fi

exit 0
