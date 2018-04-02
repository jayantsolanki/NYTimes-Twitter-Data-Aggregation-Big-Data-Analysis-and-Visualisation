# -*- coding: utf-8 -*-
#!/usr/bin/env python   
#the above just indicates to use python to intepret this file

# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
# 
# ---------------------------------------------------------------

import sys             #a python module with system functions for this OS
from nltk.corpus import stopwords
stop_word_list = stopwords.words('english')
#  to quickly test if a word is not a stop word, use a set:
stop_word_set = set(stop_word_list)
# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
for line in sys.stdin:  

#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
    keys = line.split()  #split line at blanks (by default), 
                         #   and return a list of keys
    for key in keys:     #a for loop through the list of keys
        value = 1
        key=key.strip('"')
        key=key.strip('.')
        key=key.strip('“')
        key=key.strip('$')
        key=key.strip('?')
        key=key.strip(',')
        key=key.strip(')')
        key=key.strip('(')
        key=str.replace(key,'\'s','')
        key=str.replace(key,'\\','')
        key=str.replace(key,'s\'','')
        if(key[:1].isdigit() or key[:1]=='$' or key[:1]=='&'):
            continue
        if key.lower() not in stop_word_set:
            print('{0}\t{1}'.format(key, value) ) #the {} is replaced by 0th,1st items in format list
                            #also, note that the Hadoop default is 'tab' separates key from the value
