from  random import *
from  hangman_ascii_art import *
lives=6


rand_word=choice(guess_list)
print(rand_word)

# max_tries=5
# max_tries=int(max_tries)
# for i in range(len(guess_list)):
word_list=[]
blanks=[]
for i in rand_word:
    blanks.append('_')
print(logo)
print(blanks)

while '_' in blanks:
    x = input("Guess a letter in the word? ").lower()

    # for i in rand_word_list:
    #     if i==x:
    #         word_list.append('Right')
    #     else:
    #         word_list.append('Wrong')
    # print(word_list)

    # or blanks = ['_'] * len(rand_word)
    # for i in rand_word_list:
    #     if i==x:
    #         index = rand_word_list.index(i)
    #         blanks[index] = x
    # Using rand_word_list.index(i) inside the loop will result in a linear search for the index of the
    # element i within rand_word_list. This means that if the same character appears multiple times in rand_word_list,
    # the index function will always return the index of the first occurrence, leading to incorrect behavior.
    # so do the loop like this:
    for i in range(len(rand_word)):
        if rand_word[i] == x:
            blanks[i] = x
            if x in blanks:
                print(f"You guessed the letter {x} already")
        if '_' not in blanks:
            print("you win")
    #condo to reduce lives hould not be in the for loop cos
    # if you decrement it means you will decrement on every iteration you barb
    if x not in rand_word:
        lives-=1

        if lives == 0:
            print("YOU LOSE HANGMAN!!!!!!!!!!!!!!!")
            print(stages[6 - lives])
            break
        else:
            print(stages[6-lives])
            print(f"The letter {x} does not exist")
            print(f"try again. Num lives left: {lives}")
    print(blanks)
