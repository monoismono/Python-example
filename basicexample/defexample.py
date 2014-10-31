#!/usr/bin/python
# Code example create by mono
# 2014.10.30
# this py is for basic example


print( 'this is example for how to def()\n' )

def str_test( name ) :
    if name == "mono" :
       print( 'Hi mono' )
    else :
       print( 'Who are you?')

def num_test( x , y ) :
    if x > y :
       print( str( x ) + " > " + str( y ) )
    elif x < y :
       print( str( x ) + " < " + str( y ) )
    else :
       print( str( x ) + " = " + str( y ) )

print( 'result of str_test( mono ) is ' )
str_test( 'mono' )
print( 'result of str_test( nono ) is ' )
str_test( 'nono' )
print( 'result of num_test( 1 , 2 ) is ' )
num_test( 1 , 2 )
print( 'result of num_test( 2 , 1 ) is ' )
num_test( 2 , 1 )
print( 'result of num_test( 1 , 1 ) is ' )
num_test( 1 , 1 )
print( ' ' )

raw_input()
