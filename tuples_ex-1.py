# Create an empty tuple
emptytuple = ()

# Create a tuple containing names of sisters and brothers
sisters = ('mahi','rahi')

brothers = ('manav','nishu')

#  Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# Displays the no. of siblings
totalsiblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to familymembers
father = 'Prakash'
mother = 'Pinky'
familymembers = (father, mother) + siblings

# Display results after such operations
print("Empty Tuple:", emptytuple)
print("Sisters:", sisters)
print("Brothers:", brothers)
print("Siblings:", siblings)
print("Number of Siblings:", totalsiblings)
print("Parents: ","Father-", father ,"Mother-",mother)
print("Family Members:", familymembers)