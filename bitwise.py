a = 13
b = 5

#& (AND) (both left side and right side must be True)
if a>b and a>10:
    print("This is an AND")
    
#| (OR) (if left side or right side is True)
if a>b or a < 10:
    print("This is an OR")
    
#! (NOT) (negates the rest of the expression)
if a != b:
    print ("This is a BITWise Negate statement")
