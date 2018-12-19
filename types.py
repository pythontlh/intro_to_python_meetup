#print("1" + 1) # comment this line out to run the rest of the program
# uncomment the above to see what type of error you get when there's a type mismatch

Age = input ("How old are you in years?: ")
type(Age)

whatami = (type(Age))
print("\nI am a", whatami, "by default")

print ("\nI turn this into a integer with int(Age)")
castAge = int(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)

print ("\nI turn this into a float with float(Age)")
castAge = float(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)

print ("\nI turn this into a string with str(Age)")
castAge = str(Age)
whatami = (type(castAge))
print(whatami)
print(castAge)
