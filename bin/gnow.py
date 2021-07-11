#!/usr/bin/env python3

# Import text color class.
from module import colorClass
Color = colorClass.ColorClass()

# Import conditional class.
from module import conditionalClass
Conditional = conditionalClass.ConditionalClass()

# Import main class.
from module import mainClass
Main = mainClass.MainClass()



if Conditional.repository_exists() == 0:
  Color.set('No git repository exists in this directory.', 'red', 'white')
else:
  #Color.set('green', 'arugana')
  Main.fast_commit()
