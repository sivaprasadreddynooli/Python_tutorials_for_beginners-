import re

#placing r in front will take whole string as raw character
string = "i am good\ni am from kadapa"
print(string)
string2 = r"i am good\ni am from kadapa"
print(string2)


#The way the match() method works is that it will only find matches if they occur at the
# start of the string being searched.
m = re.match(r'i have','i have a cat')
print(m.group(0))


#The search() method is similar to match(), but search() doesn’t restrict us to only finding
#  matches at the beginning of the string,
m = re.search(r'cat','i have a cat and a dog')
print(m.group(0))


#when we call findall(), we simply get a list of all matching patterns
li = re.findall(r'good','good things happen to good people')
print(li)


#Group by Number Using match.group

string = 'Doe, John: 555-1212'
#By surrounding certain parts of the regular expression in parentheses (the ‘(‘ and ‘)’ characters),
# we can group the content and then work with these individual groups.
match = re.search(r'(\w+), (\w+): (\S+)', string)
#These groups can be fetched using the match object’s group() method. The groups are addressable
#numerically in the order that they appear, from left to right, in the regular expression
#(starting with group 1):
#The reason that the group numbering starts with group 1 is because group 0 is reserved to hold the entire match
print(match.group(1))
print(match.group(2))
print(match.group(3))

