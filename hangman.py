def hangman(guess):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rem_letters = list(guess)
    board = ["_"]*len(guess)
    win = False
    print("Welcome to hangman")
    while wrong < len(stages)-1:
        print("\n")
        lo = input("Guess a letter: ")
        if lo in rem_letters:
            rep = rem_letters.index(lo)
            board[rep] = lo
            rem_letters[rep] = '$'
        else:
            wrong+=1
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose!, It was " + guess)
import random
lists = ["baby","large","muscle","puppy","ramdom"]
o = random.choice(lists)
hangman(o)
