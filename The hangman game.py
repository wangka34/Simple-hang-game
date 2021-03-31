def check_number(number):
    while True:
        try:
            Input = int(input(number))
            if Input < 1:
                raise ValueError
        except ValueError:
            print("Your input is not proper, please input again")
            continue
        else:
            return Input 
            break 

Word_length = check_number("how many letters in this words? please input an integer: ")

def attempts_compute(word):
    if word < 10:
        print('I will have 15 attempts')
        return 15
    elif word >= 10 and word <= 20:
        print('I will have 18 attempts')
        return 18
    else:
        print('I will have 21 attempts')
        return 21


attempts = attempts_compute(Word_length)

import random
import string
letter_list = list(string.ascii_lowercase)

def check_answer(letter):
    while True:
        try:
            Input = input(letter)
            if not (Input == 'y' or Input == 'n'):
                raise ValueError
        except ValueError:
            print("Your input is not proper, please input again")
            continue
        else:
            return Input 
            break 

def check_position(number):
    while True:
        try:
            Input = int(input(number))
            if not (Input - 1) in guessed_position:
                raise ValueError
        except ValueError:
            print("Your input is not proper, please input again")
            continue
        else:
            return Input 
            break 

def listtoString(guess_list):  
    word = ""  
    for ele in guess_list:  
        word += ele   
    return word  

guess_letter_list = list('_'*Word_length)
 
guessed_position = list(range(Word_length))

i = 0
while i < attempts:
    my_guess_letter = random.choice(letter_list)
    my_guess = 'is ' + my_guess_letter + ' in the word? Please answer y or n: '
    user_answer = check_answer(my_guess)
    if user_answer == 'y':
        the_position = check_position('What is the position of this letter? Please input an integer: ')
        guess_letter_list[the_position-1] = my_guess_letter
        guessed_position.remove(the_position-1)
        while check_answer('Does this letter have more positions? Please answer y or n: ') == 'y':
            the_position = check_position('What is the position of this letter? Please input an integer: ')
            guess_letter_list[the_position-1] = my_guess_letter
            guessed_position.remove(the_position-1)
            if guessed_position == []:
                break
        if guessed_position == []:
            the_answer = listtoString(guess_letter_list)
            print('Yes! I win! The word is',the_answer)
            break
        guess_letter = listtoString(guess_letter_list)
        print('I have',len(guessed_position),'letters to guess, now I have', guess_letter)
        letter_list.remove(my_guess_letter)
        i = i + 1
        left = attempts - i
        print('I have',left,'more times to guess')
        if i == attempts:
            print('I lost, you win')
    elif user_answer == 'n':
        letter_list.remove(my_guess_letter)
        i = i + 1
        left = attempts - i
        print('I have',left,'more times')
        if i == attempts:
            print('I lost, you win')
            break
        print('let me guess again')
    
print('Thank you for playing')
thanks = input('press enter to exit')