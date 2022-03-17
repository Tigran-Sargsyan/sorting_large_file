import random

with open(r"C:\Users\sargs\Рабочий стол\sorting\nums.txt","w") as main_file:
    # Opening 20 file to store the parts of the main file and sort independently
    chunk1 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk1.txt", "w")
    chunk2 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk2.txt", "w")
    chunk3 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk3.txt", "w")
    chunk4 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk4.txt", "w")
    chunk5 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk5.txt", "w")
    chunk6 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk6.txt", "w")
    chunk7 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk7.txt", "w")
    chunk8 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk8.txt", "w")
    chunk9 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk9.txt", "w")
    chunk10 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk10.txt", "w")
    chunk11 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk11.txt", "w")
    chunk12 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk12.txt", "w")
    chunk13 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk13.txt", "w")
    chunk14 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk14.txt", "w")
    chunk15 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk15.txt", "w")
    chunk16 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk16.txt", "w")
    chunk17 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk17.txt", "w")
    chunk18 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk18.txt", "w")
    chunk19 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk19.txt", "w")
    chunk20 = open(r"C:\Users\sargs\Рабочий стол\sorting\chunk20.txt", "w")

    for i in range(1000000000):
        current = str(random.randint(0, 121)) + " "
        if i<50000000:
            chunk1.write(current)
        elif i>= 50000000 and i<100000000:
            chunk1.close()
            chunk2.write(current)
        elif i>=100000000 and i<150000000:
            chunk2.close()
            chunk3.write(current)
        elif i>=150000000 and i<200000000:
            chunk3.close()
            chunk4.write(current)
        elif i>=200000000 and i<250000000:
            chunk4.close()
            chunk5.write(current)
        elif i>=250000000 and i<300000000:
            chunk5.close()
            chunk6.write(current)
        elif i>=300000000 and i<350000000:
            chunk6.close()
            chunk7.write(current)
        elif i>=350000000 and i<400000000:
            chunk7.close()
            chunk8.write(current)
        elif i>=400000000 and i<450000000:
            chunk8.close()
            chunk9.write(current)
        elif i>=450000000 and i<500000000:
            chunk9.close()
            chunk10.write(current)
        elif i>=500000000 and i<550000000:
            chunk10.close()
            chunk11.write(current)
        elif i>=550000000 and i<600000000:
            chunk11.close()
            chunk12.write(current)
        elif i>=600000000 and i<650000000:
            chunk12.close()
            chunk13.write(current)
        elif i>=650000000 and i<700000000:
            chunk13.close()
            chunk14.write(current)
        elif i>=700000000 and i<750000000:
            chunk14.close()
            chunk15.write(current)
        elif i>=750000000 and i<800000000:
            chunk15.close()
            chunk16.write(current)
        elif i>=800000000 and i<850000000:
            chunk16.close()
            chunk17.write(current)
        elif i>=850000000 and i<900000000:
            chunk17.close()
            chunk18.write(current)
        elif i>=900000000 and i<950000000:
            chunk18.close()
            chunk19.write(current)
        else:
            chunk19.close()
            chunk20.write(current)


        main_file.write(current)
        main_file.write(" ")
    chunk20.close()
