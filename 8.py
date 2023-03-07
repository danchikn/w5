import re

f = open('row.txt', encoding = "utf8") 

x = True

while x:
    f_line = f.readline()
    
    if f_line:
        print(re.findall('[А-Я][^А-Я]*', f_line))
    
    if not f_line:
        print("Not matched!")
        x = False
f.close()

    