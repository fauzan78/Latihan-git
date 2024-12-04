import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


Papper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
map = [Rock, Papper,Scissor]
Choice1 = int(input("Masukkan pilihan mu?\n1. Rock\n 2.Paper \n3. Scissor\n")) - 1
print(f"Your Choice{map[Choice1]}")
bot = random.randint(0, 2)
print(f"bot Choice{map[bot]}")
if Choice1 <= 2 or Choice1 >= 0:
    if Choice1 == 0 and bot == 2 :
        print("You WON")
    elif Choice1 == 2 and bot == 0 :
        print("You Lose")
    elif Choice1 == 0 and bot == 0 :
        print("Draw")
    elif Choice1 == 1 and bot == 0 :
        print("Win")
    elif Choice1 == 1 and bot == 1 :
        print("Draw")
    else : 
        print("Belum dIBUAT")
else :
    print("Print yang benr tolol")
    
