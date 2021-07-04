import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_______     ",
              "|     |     ",
              "|   (T^T)   ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",]

    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman.")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Let's think 1moji. "
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"

        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You Win.")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose.The answer is {}.".format(word))



word_list = ["Python", "Java", "computer", "hacker", "painter"]
random_number = random.randint(0, 4)
ans = word_list[random_number]


hangman(ans)

    
    
