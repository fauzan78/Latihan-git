angka = [123,121,323,231]
listbaru=[]

while angka:
    templist = angka[0]
    for i in range(len(angka)):
        if angka[i] < templist :
            templist = angka[i]
    listbaru.append(templist)
    angka.remove(templist)
print(listbaru)