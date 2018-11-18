line = r"rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash"

username = line[0:7]
group = line[8:9]
uid = line[10:14]
gid = line[15:19]
name = line[20:31]
home = line[32:46]
shell = line[47:56]
print("{} {} {} {} {} {} {}".format(username,group,uid,gid,name,home,shell))

print(line.split(":"))
