count = 0
total = 0
while count < 5:
    title = input("Enter Book Title: ")
    cost = input("Enter Book Cost: ")

    total += float(cost)
    print("{}\t\t{}\t{:.2f}".format(title,cost,total))
    count+=1

