lst = [0] * 121
sorted_list = open(r"C:\Users\sargs\Рабочий стол\sorting\sorted.txt","w")

def counter(filename):
    file1 = open(r"C:\Users\sargs\Рабочий стол\sorting\{fname}".format(fname=filename))
    file = list(file1)
    file = file[0].split()
    for i in range(len(file)):
        file[i] = int(file[i])

    for i in range(121):
        lst[i] += file.count(i)

    file1.close()

chunk1 = "chunk1.txt"
counter(chunk1)
chunk2 = "chunk2.txt"
counter(chunk2)
chunk3 = "chunk3.txt"
counter(chunk3)
chunk4 = "chunk4.txt"
counter(chunk4)
chunk5 = "chunk5.txt"
counter(chunk5)
chunk6 = "chunk6.txt"
counter(chunk6)
chunk7 = "chunk7.txt"
counter(chunk7)
chunk8 = "chunk8.txt"
counter(chunk8)
chunk9 = "chunk9.txt"
counter(chunk9)
chunk10 = "chunk10.txt"
counter(chunk10)
chunk11 = "chunk11.txt"
counter(chunk11)
chunk12 = "chunk12.txt"
counter(chunk12)
chunk13 = "chunk13.txt"
counter(chunk13)
chunk14 = "chunk14.txt"
counter(chunk14)
chunk15 = "chunk15.txt"
counter(chunk15)
chunk16 = "chunk16.txt"
counter(chunk16)
chunk17 = "chunk17.txt"
counter(chunk17)
chunk18 = "chunk18.txt"
counter(chunk18)
chunk19 = "chunk19.txt"
counter(chunk19)
chunk20 = "chunk20.txt"
counter(chunk20)

for i in range(len(lst)):
    for j in range(lst[i]):
        sorted_list.write(str(i))
        sorted_list.write(",")

print(lst)
sorted_list.close()
