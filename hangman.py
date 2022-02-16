import random
list1 = ['хер', 'член', 'нога', 'рука', 'жопа', 'глаз']
word = random.choice(list1)


def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "        |       ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = int(rletters.index(char))
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            print(rletters)
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
    print(f"Вы проиграли! Слово было: {word}.")

hangman(word)