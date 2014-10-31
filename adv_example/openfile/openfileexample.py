#!/usr/bin/python
# coding = UTF-8
# Code example create by mono
# 2014.10.30
# this py is for open file 

print( 'This is a example to open file.\n' )
filename = raw_input( 'please enter filename : ' )

if len( filename ) > 0 :
    f = open( filename , 'r' )
    b_str = f.read()
    f.close
    print b_str.decode( 'utf-8' )
    print b_str.decode( 'utf-8' ).encode( 'utf-8' )
else :
    print('\nyou didnt enter filename , please enter filename.')

raw_input()




