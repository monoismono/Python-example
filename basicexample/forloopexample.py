#!/usr/bin/python
# Code example create by mono
# 2014.10.30
# this py is for basic example


print( 'this is example for python loop\n' )

def hi( name ):
    print( 'Hi ' + name )
people = [ 'Mono', '601', 'Cy', 'Candy']

#This is for loop on string list

print( 'for loop on string list example' )    


for name in people :
    hi(name)
    print( 'Next people' )
print( ' ' )



#This is for loop on num

print( 'while loop on int example' )
for i in range( 10 , 0 , -1 ) :
    print( i )
print( ' ' )

#This is for while loop on str-list
print( 'while loop on str list example ' )
i = 0
while not people[ i ]  :
    print( 'peoplo in list is ' + str( people[ i ] ))
    i += 1
else :
    print( 'there is no people on list ')

print( '' )

raw_input()
