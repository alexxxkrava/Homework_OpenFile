for i in range(1, 4):
    doc = str(i)+'.txt'
    with open(doc, 'r+', encoding='UTF-8') as f:
        res = f.read()
        with open('4.txt', 'a', encoding='UTF-8') as file:
            file.write(doc + '\n')
            file.write(res + '\n')
print(file)

