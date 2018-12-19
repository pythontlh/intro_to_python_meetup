#print("1" + 1) # comment this line out

Age = input ("How old are you in years?: ")
type(Age)

whatami = (type(Age))
print(whatami)

print ("I turn this into a string")
castAge = str(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)

Age = input ("How old are you in years?: ")
print ("I turn this into a integer")
castAge = int(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)

print ("I turn this into a float")
castAge = float(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)
