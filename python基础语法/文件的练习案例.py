f = open('/bill.txt', 'r', encoding='UTF-8')
# text = f.read()
# print(f"{text}")

k = open('/bill.txt.bak', 'w', encoding='UTF-8')
for x in f:
    x = x.strip()
    if x.split(',')[4] == '测试':
        continue
    k.write(x)
    k.write("\n")
    # for word in words:
    #     if word == '测试':
    #         break
    #     else:
    #         k.write(x)
    #         k.write("\n")
f.close()
k.close()
