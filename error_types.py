## Uncomment each print statement one at a time to see the type of error

## Syntax - code doesn’t conform to language rules
#print ("Python is cool!)
## (missing a “ - generates a Syntax Error "EOL while scanning string literal" )

##Runtime - errors during execution
#print (x)
##(Generates "NameError: name 'x' is not defined" - meaning x is not defined)

##Semantic- program performs unexpectedly (the hardest to find)
#print (5 - 2 *10 )
##(you get -15 as the output, not the 30 you were expecting)
