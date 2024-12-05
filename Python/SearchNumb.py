number = input("Put your array? ")
angka = list(map(int, number.split(",")))
finds = int(input("Put Your Number ? "))
findnums = False
count = 0
while not findnums :
    for i in angka:
        count += 1
        if i == finds :
            findnums = True
            break
    if not findnums:
        print("sERIOUS!!!")
        break
print(f"How many comp = {count}")