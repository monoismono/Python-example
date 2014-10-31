#!/usr/bin/python
# Code example create by mono
# 2014.10.30
# this py is for basic example


print( 'This is example for python if...else \n' )

x = 1
y = 2

if x > y :
  print( 'x > y is ' + str( x > y ) )
elif x == y :
  print( 'x = y is ' + str( x == y ) )
else :
  print( 'x < y is ' + str( x < y ) )

print( ' ' )

name = 'mono'

if name == 'mono' :
  print( 'Hi mono ' )
elif name == 'nomo' :
  print( 'Hi nomo ' )
else :
  print( 'Hi nono ' )

print( ' ' )

raw_input()
