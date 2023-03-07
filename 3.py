import re

f = open('row.txt', encoding = "utf8") 

def text_match(txt):
    pat = '^[а-я]+_[а-я]+$'
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True

while x:
    f_line = f.readline()
    
    if text_match(f_line):
        print(f_line)
        
    if not f_line:
        print("Not matched!")
        x = False
f.close()

    