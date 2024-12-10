import random

word = ["Item", "Run"]
choosen_word = random.choice(word).lower()
display = ["_" for _ in choosen_word] 
print(" ".join(display))

Health = 3
while Health > 0:

    if "_" not in display:
        print("You won!")
        break

    user = input("Your Guess: ").lower()

    if user not in choosen_word:
        Health -= 1
        print(f"Wrong guess! Health remaining: {Health}")
        if Health == 0:
            print("You lose. The word was:", choosen_word)
    else:
        for i in range(len(choosen_word)):
            if user == choosen_word[i]:
                display[i] = user
        print(" ".join(display))
