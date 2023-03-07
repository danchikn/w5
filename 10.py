def camel_to_snake(camel_string):
    snake_list = []
    for i, c in enumerate(camel_string):
        if c.isupper() and i > 0:
            snake_list.append('_')
        snake_list.append(c.lower())
    return ''.join(snake_list)


f = open('row.txt', encoding="utf8")

x = True

while x:
    f_line = f.readline()
    f_line = "".join(f_line.split())
    print(camel_to_snake(f_line))

    if not f_line:
        print("End Of File")
        x = False

f.close()