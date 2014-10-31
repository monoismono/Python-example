#!/usr/bin/python
# coding = UTF-8
# Code example create by mono
# 2014.10.30
# this py is for open file
print( 'This is a example to open file.\n' )

import sys
if len(sys.argv) < 2 :
    print( 'please use command like $./openfileexample_2.py filename \n' )
else :
    file = open(sys.argv[1] , 'r' )
    content = file.read()
    print content
    file.close

raw_input()

