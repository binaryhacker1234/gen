#!/usr/bin/python
import sys, random

def passGenVars(words, minchars, maxchars):
  workspace = []
  comblist = []
  for i in random.randrange(minchar, maxchar):
    variables = random.randrange(1, i)
    n = 1
    while n < i:
      if len(list(words[i])) % i == 0:
        for each in list(str(len(list(words[i])) / i)):
          comblist.append(each)
      else:
        workspace.append(len(list(words[i])) % i)
        
        
        
        
