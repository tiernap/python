import random


names1 = ['Joe', 'John', 'Jane', 'Mick', 'Mary', 'Ann', 'Rick', 'John', 'Aine', 'Brenda']
names2 = ['Jack', 'Mary', 'Phil', 'John', 'Pat', 'Joe', 'Luke', 'Bill', 'Ben', 'Nathan']
randlist1 = []
randlist2 = []

for i in range(0, 10):
    randlist1.append(random.randint(1, 20))
    randlist2.append(random.randint(1, 20))

dict1 = dict(list(zip(names1, randlist1)))
dict2 = dict(list(zip(names2, randlist2)))

print(dict1)
print(dict2)

# 1: find names list intersection
intersection = []

for i in names1:
    if i in names2:
        intersection.append(i)

print("These people have purchased tickets on both weeks: {}".format(intersection))

# 2: find most popular numbers
popularity_list = []
combined_numbers = randlist1+randlist2

for i in combined_numbers:
    popularity_list.append((i,combined_numbers.count(i)))
    combined_numbers.remove(i)


def return_second(element):
    return element[1]


popularity_list.sort(key=return_second)
popularity_list.reverse()
print("the most popular numbers are: ")
for i in popularity_list:
    print("{}:\t{} times".format(i[0],i[1]))

# 3: find people who used same number on both weeks
for i in intersection:
    if dict1[i] == dict2[i]:
        print("{} picked number {} on both weeks".format(i,dict1[i]))