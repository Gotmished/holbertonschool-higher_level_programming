#!/usr/bin/python3
# result = ""
#for i in range(97, 123):
#    result = result + chr(i)
#
#print(result)

for i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(i), end="")
