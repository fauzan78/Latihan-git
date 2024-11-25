
test_str = "Carson Chua Kai Shen"
print("Name " + (test_str) + " Student Id : 2024030445")
ASCIIs = input("Input Your Name : ")
Choice = input(" 1. Binary \n 2.Hex\nWhat U want ? " )
if Choice == "1" :
    for i in bytearray(ASCIIs,encoding='utf-8'):
        print("01010000")
        print("00000000"+format(i, '08b'))

elif Choice == "2":
    for i in bytearray(ASCIIs,encoding='utf-8'):
        print("50")
        print("00"+format(i, '02x'))
else :
    print("Wrong Choice")