import re

f = open('row.txt', 'r', encoding = "utf8") 

def tmt(txt):
    pat = ''.join(x.capitalize() or '_' for x in txt.split('_'))
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True

while x:
    f_line = f.readline()
    
    if tmt(f_line):
        print(f_line)
        
    if not f_line:
        print("not such file or end file")
        x = False
f.close()

    