number = input("Put your array? ")
angka = list(map(int, number.split(",")))
finds = int(input("Put Your Number ? "))
count = 0
low = 0
high = len(angka) - 1
mid = 0
while low <= high :
    count += 1
    mid = (high + low) // 2
    if angka[mid] == finds :
        print(f"Found Number {finds} on index {mid}")
        print(count)
        break
    elif angka[mid] >= finds:
        high = mid - 1
    else:
        low = mid + 1