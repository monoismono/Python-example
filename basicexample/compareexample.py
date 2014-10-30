# Code example create by mono
# 2014.10.30
# this py is for basic example

import os
print( 'this is example for python var compare\n' )

# for test compare results

print( 'compare results' )
print( '5 > 2 is ' + str( 5 > 2 ) )
print( '1 > 3 is ' + str( 1 > 3 ) )
print( '1 = 1 is ' + str( 1 == 1 ) )
print( '6 = 12 / 2 is ' + str( 6 == 12 / 2 ) )
print( '6 > 2 & 1 < 3 is ' + str( 6 > 2 and 1 < 3 ) )
print( '3 > 2 & 2 < 1 is ' + str( 3 > 2 and 2 < 1 ) )
print( '3 > 2 | 2 < 1 is ' + str( 3 > 2 or 2 < 1 ) )
print( ' ' )

# for test bool results
print( 'bool test' )
test_bool = True
print( 'test_bool is ' + str( test_bool ) )
test_bool = 1 > 2
print( "test_bool's value about 1 > 2 is " + str( test_bool ) )
print( 'True and True is ' + str( True & True ) )
print( ' ' )

os.system( 'pause' )
