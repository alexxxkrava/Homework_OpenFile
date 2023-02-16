total = 0
res = {}
res1 = []
for i in range(1, 4):
    doc = str(i)+'.txt'
    f = open(doc, 'r+', encoding = 'UTF 8')
    for line in f:
        total += 1
    res[doc] = total
    res1.append(total)
    total = 0
    f.close()
res1.sort()
with open('4.txt', 'w', encoding = 'UTF 8') as file:
    for i in res1:
        for key, val in res.items():
            if val == i:
                file.write(key + '\n')
                file.write(str(i) + '\n')
                with open(key, 'r+', encoding = 'UTF 8') as file_:
                    a = file_.read()
                    file.write(a + '\n')







