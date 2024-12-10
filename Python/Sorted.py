number = input("Put your array? ")
angka = list(map(str,number.split(",")))
finds = input("Put Your Number ? ")
findnums = False
count = 0
listbaru = []
while angka :
    tempo = angka[0]
    for i in range(len(angka)):
        if angka[i][0] < tempo[0] :
            tempo = angka[i]
    listbaru.append(tempo)
    angka.remove(tempo)
print(f"Sorted List: {listbaru}")
print(f"How many comparisons = {count}")
print(f"Number {finds} {'found' if findnums else 'not found'} in the list.")