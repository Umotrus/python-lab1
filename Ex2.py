
# Exercise 2

s = input("Insert input string: ")
l = s.__len__()

if l < 2:
    res = ""
else:
    res = s[0] + s[1] + s[l-2] + s[l-1]

print("result: %s" % res)
