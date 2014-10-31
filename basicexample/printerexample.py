#!/usr/bin/python
# Code example create by mono
# 2014.10.30
# this py is for basic example


print( 'this is example for python basic\n' )

# print string & calculate

print( 'only show the calculate result' )
print( 2+3 )
print( 4*5 )
print( 5-1 )
print( 1024*768 )
print( ' ' )

#combin string & caiculate result

print( 'show result & process' )
print( '2+3=' + str( 2+3 ) )
print( '4*5=' + str( 4*5 ) )
print( '5-1=' + str( 5-1 ) )
print( '1024*768=' + str( 1024*768 ) )
print( ' ' )

#simple string example

print( 'something about string' )
print( 'Hello world')
print( 'mono')
print( 'Hellp world '+'mono')
print( 'mono' * 3 )
print( 'mono'.upper() )
print( ' ' )

#simple len test

print( 'something about len')
print( 'len of mono is ' + str( len( 'mono' ) ) )
print( 'len of 123456 is ' + str ( len ( str( 123456 ) ) ) )
print( ' ' )

#simple Var example

print( 'something about Variables')
name = 'mono'
a=1
b=2
print( 'name is ' + name )
print( 'a is ' + str( a ) )
print( 'b is ' + str( b ) )
print( 'a*b is ' + str ( a * b ) )
print( ' ' )

#simple list example

print( 'something about list' )
testlist = [ 1, 31, 29, 123, 9]
print( 'listtest is ' + str( testlist ) )
testlist.sort()
print( 'listtest by sort is ' + str( testlist ) )
testlist.reverse()
print( 'listtest by reverse is ' + str( testlist ) )
testlist.append(39)
print( 'listtest by append 39 is ' + str( testlist ) )
testlist.remove(1)
print( 'listtest by remove 1 is ' + str( testlist ) )
print( 'list[0] is ' + str( testlist[ 0 ] ) )
print( ' ' )

#simple Dictionaries example

print( 'something about Dictionaries' )
dict = { 'name' : 'mono' ,
         'country' : 'Taiwan' ,
         'favorite_number' : [ 1, 2, 3, ] }
print( 'Dictionaries name is ' + dict[ 'name' ] )
print( 'Dictionaries list is ' + str( dict[ 'favorite_number' ] ) )
dict[ 'lang' ] = 'chinese'
print( 'Add language to Dictionaries, language is ' + dict[ 'lang' ] )
dict[ 'name' ] = '601'
print( 'Modify Dictionaries name is ' + str( dict ) )
del dict[ 'favorite_number' ]
print( 'Remove Dictionaries favorite_number is ' + str( dict ) )
print( ' ' )

raw_input()
