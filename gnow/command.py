#!/usr/bin/env python3
import sys
import re

from .color import ColorClass
from .check import CheckClass
from .main import MainClass

Color = ColorClass()
Check = CheckClass()
Main  = MainClass()

#------------------------------
# Command arguments
#------------------------------

def run():
    if len(sys.argv) >= 2:
        arg1 = sys.argv[1]
    else:
        arg1 = 0
    if len(sys.argv) >= 3:
        arg2 = sys.argv[2]
    else:
        arg2 = 0
    if len(sys.argv) >= 4:
        arg3 = sys.argv[3]
    else:
        arg3 = 0
    
    if Check.repository_exists() == 0:
        Color.set(' No git repository exists in this directory. ', 'red', 'white')
        exit()
    
    #Color.set('green', 'arugana')
    # Help
    if arg1 == '-h' or arg1 == '--help':
        Main.usage()
        exit()
    # Version
    elif arg1 == '-v' or arg1 == '-V' or arg1 == '--version':
        print('0.0.1')
        exit()
    # Commit only
    elif arg1 == '-c' or arg1 == '--commit':
        if arg2 == 0 or re.compile('^-.+').search(arg2):
            Main.fast_commit()
        else:
            Main.fast_commit(arg2)
    # Tagging
    elif arg1 == '-t' or arg1 == '--tag':
        if arg2 == 0 or re.compile('^-.+').search(arg2):
            Main.fast_tag()
        else:
            Main.fast_tag(arg2)
    # Status
    elif arg1 == '-s' or arg1 == '--status':
        Check.status()
    elif arg1 == '-' or arg1 == '--':
        Color.set("Illegal option: Only '-' or '--'",'red')
        exit()
    # Logo
    elif arg1 == '-l':
        print(''' _  _  _   
(_|| |(_)VV
 _| 0.0.1''')
    # Undefined option
    elif arg1 != 0 and re.compile('^-.*').search(arg1):
        Color.set("Illegal option: Undefined option '" + arg1 + "'",'red')
    # No arguments
    elif arg1 != 0 and re.compile('^(?!-.+)').search(arg1):
        Main.fast_push(arg1)
    # Without any arguments
    elif arg1 == 0:
        Main.fast_push()
    else:
        exit()

if __name__ == '__main__':
    run()
