#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

f = open('row.txt','r', encoding = "utf8") 

x = True
while x:
    f_line = f.readline()
    
    if f_line:
        print(re.sub("[ ,.]", ":", f))
    
    if not f_line:
        print("Not matched!")
        x = False
f.close()

    