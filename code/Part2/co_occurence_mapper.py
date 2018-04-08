#!/usr/bin/env python  
# -*- coding: utf-8 -*- 
#the above just indicates to use python to intepret this file

# ---------------------------------------------------------------
#This mapper code will input a line of text and output <(word,co_occurenceword), 1>
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
    words = line.split()  #split line at blanks (by default), 
                         #   and return a list of keys
    value = 1

    final_words = []
    for word in words:     #a for loop through the list of keys
        word=word.strip('"')
        word=word.strip('.')
        word=word.strip('“')
        word=word.strip('$')
        word=word.strip('?')
        word=word.strip(',')
        word=word.strip(')')
        word=word.strip('(')
        word=str.replace(word,'\'s','')
        word=str.replace(word,'\\','')
        word=str.replace(word,'s\'','')
        if(word[:1].isdigit() or word[:1]=='$' or word[:1]=='&'):
            continue
        if word.lower() not in stop_word_set:
            final_words.append(word.lower())

    if len(final_words):
        final_words = set(final_words)
        final_words = list(final_words)
        final_words.sort()
        count = len(final_words)
        for i in range(count):
	    if i < count-1:
                for co_word in final_words[i+1:]:
                    print('{0}\t{1}'.format((final_words[i],co_word), value) )