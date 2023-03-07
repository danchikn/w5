import re

f = open('row.txt', encoding = "utf8") 

x = True

while x:
    f_line = f.readline()
    
    if f_line:
        print(re.sub(r"(\w)([A-Z])" or "(\w)([А-Я])", r"\1 \2", f_line))
    
    if not f_line:
        print("Not matched!")
        x = False
f.close()

    