
import time

def load_valid_words():
    valid_words = []

    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            valid_words.append(line)

    return valid_words 

def play_letters():
    print("Lets play a letter round!")
    letters = []

    #loop to ask player
    for i in range(3):
        v = input('select a vowel: ')
        letters.append(v)
    for i in range(4):
        c = input('select a consonant: ')
        letters.append(c)
    for i in range(2):
        w = input('select a letter: ')
        letters.append(w)
    print(letters)

    #start timer
    x = 30
    for i in range(x):
        print(x-i, end=" ", flush=True)
        time.sleep(1)
    print()
    print("timer is up")
    #take input from player 1: what is your word
    answer_p1 = input('player 1: what is your word: ')
    answer_p2 = input('player 2: what is your word: ')

    valid_words = load_valid_words()

    if answer_p1 in valid_words:
        len_p1 = len(answer_p1)
    else:
        len_p1 = 0
    
    if answer_p2 in valid_words:
        len_p2 = len(answer_p2)
    else:
        len_p2 = 0



    score_p1 = 0
    score_p2 = 0
    if len_p1 > len_p2:
        print('player 1 win')
        score_p1 = len_p1
        if len_p1 == 9:
            score_p1 = score_p1 + 9
    elif len_p1 < len_p2 :
        print('player 2 win')
        score_p2 = len_p2
        if len_p2 == 9:
            score_p2 = score_p2 + 9
    else:
        print('draw')
        score_p1 = len_p1
        if len_p1 == 9:
            score_p1 = score_p1 + 9
        score_p2 = len_p2
        if len_p2 == 9:
            score_p2 = score_p2 + 9

    print(f'player 1 score:{score_p1}')
    print(f'player 2 score:{score_p2}')

    return(score_p1,score_p2) 



if __name__ == "__main__":
    play_letters()
    
