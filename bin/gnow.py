#!/usr/bin/env python3

# Import text color class.
from module import colorClass
Color = colorClass.ColorClass()

# Import conditional class.
from module import conditionalClass
Conditional = conditionalClass.ConditionalClass()

if Conditional.repository_exists() == 1:
  Color.set('green', 'arugana')
else:
  Color.set('red', 'No git repository exists in this directory.')
  return 0

#if [ `echo "$(git status -s 2>&1 > /dev/null | awk '{print $1}')'" | grep '^fatal'` ]; then
#  red 'No git repository exists in this directory.'
#else
#  GIT_STATUS=`git status -s`
#  BRANCH=`git rev-parse --abbrev-ref HEAD`
#  BRANCH_EXIST=`git branch`
#  REPO_EXIST=1
#fi


