#!/usr/bin/python
# Code example create by mono
# 2014.10.30
# this py is for basic example


print( 'this is example for python class\n' )

class cat :
      def __init__( self , name , color ) :
          self.name = name
          self.color = color
      def sleep_function( self ) :
          print( self.name + ' is sleeping.')

puchu = cat( 'Puchu' , 'B&W' )
print( "my cat's name is " + puchu.name )
print( "my cat's color is " + puchu.color )
puchu.sleep_function()

raw_input()
