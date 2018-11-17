python_mission = '''The mission of  the  Python  Software  Foundation  is  to  promote,  protect,
and  advance  the  Python  programming  language,  and  to support  and  facilitate
the growth of a diverse and international community of Python programmers
'''

# Count the number of appearances of the letter s.
print("letter 's' is present {} times".format(python_mission.count('s')))

# Find the second instance of the word Python
print("Second instance of word 'python' is at position {}".format(python_mission[25:].find('Python')+25))

# what does this output? "on Softw"
print("The word returned is: {}".format(python_mission[25:34]))

# Find out if the word ‘diverse’ is in the mission statement
print("is 'diverse' present? {}".format(python_mission.find('diverse')>0))
print("is 'diverse' present? {}".format(python_mission.count('diverse')>0))

# check if "12345" is numeric
string = '12345'
print("is {} numeric? {}".format(string, string.isnumeric()))

# print path string
path = r'C:\users\ndarby\python3\python-3.5.1\bin'
print(path)
