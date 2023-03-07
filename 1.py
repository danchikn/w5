import re

f = open('row.txt', 'r', encoding = "utf8") # исправить ошибку r

def text_match(txt):
    pat = 'аб*?'
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
        print("not such file or end file")
        x = False
f.close()

    