linelen = 50
string1 = 'title'
string2 = 'A Option a'
string3 = 'b option b'
string4 = 'c option c'
print("x"*linelen)
print("<"+" "*(linelen-2)+">")
print("<"+" "*(linelen-2)+">")
print("<"+" "*(linelen-2)+">")
print("<"+" "*(linelen-2)+">")
print("<{0:^48}>".format(string1))
print("<"+" "*(linelen-2)+">")
print("<"+" "*(linelen-2)+">")
print("<  {0:<46}>".format(string2))
print("<  {0:<46}>".format(string3))
print("<  {0:<46}>".format(string4))
print("<"+" "*(linelen-2)+">")
print("<"+" "*(linelen-2)+">")
print("x"*linelen)
