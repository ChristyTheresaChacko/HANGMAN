import random
from Hangman_ui import logo,stages
print(logo)

life = 6
from Hangman_wordlist import words
chosen = random.choice(words)
find = list()
length = len(chosen)
for i in range(length):
    find +="_"
end_game = False
while not end_game:
    guess_letter = input("Guess a letter: ").lower()
    for pos in range(length):
        letter = chosen[pos]
        if letter == guess_letter:
            find[pos]= letter
    if guess_letter not in chosen:
        life -= 1
        print("Wrong Guess!!You lose a life")
        if life == 0:
            print("You lose!!")
            end_game = True
    print(f"{' '.join(find)}")
    if "_" not in find:
        print("You Win")
        end_game =True
    print(stages[life])
