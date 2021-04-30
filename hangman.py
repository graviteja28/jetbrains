import random


def play():
    random_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(random_list)
    hidden_word = list('-' * len(word))
    print("H A N G M A N")
    print()
    print(''.join(hidden_word))
    i, k = 0, set()
    while i < 8:
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower():
            print("Please enter a lowercase English letter")
        elif letter in word:
            if letter == 'a':
                z = word.index(letter)
                hidden_word[z + 2] = letter
            else:
                z = word.index(letter)
            if letter in k:
                print("You've already guessed this letter")
            elif letter == hidden_word[z]:
                print("No improvements")
                i += 1
            else:
                hidden_word[z] = letter
        else:
            if letter in k:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                i += 1
        if i != 8:
            print()
            print(''.join(hidden_word))
        k.add(letter)
        if ''.join(hidden_word) == word:
            print("You guessed the word!")
            print("You survived!")
            break
    if ''.join(hidden_word) != word:
        print("You lost!")


print('Type "play" to play the game, "exit" to quit:')
choice = input()
if choice == "play":
    play()
elif choice == "exit":
    exit()
