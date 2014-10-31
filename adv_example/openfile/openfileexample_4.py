#!/usr/bin/python
# coding = UTF-8
# Code example create by mono
# 2014.10.30
# this py is for open file
print( 'This is a example to open file.\n' )

import sys
if len(sys.argv) < 2 :
    print( 'please use command like $./openfileexample_4.py filename \n' )
else :
    print( 'this is example use for to print every line ' )
    file = open(sys.argv[1] , 'r' )
    for line in file.readlines() :
        print line
    file.close

    print( 'this is example use while to print every line ' )
    file = open(sys.argv[1] , 'r' )
    while True :
        line = file.readline()
        if not line : break
        print line
    file.close

raw_input()
