# Wordle Remake
    #### Video Demo:  https://youtu.be/BL8TDv21HQY
    #### Description: My project is a remake of the famous New York Time game, wordle.
    
    I created four functions other than main to help create the wordle remake. The first function I created is the
    choose_word function. This function reads the five_letter_word.txt which contains all of the five letter
    words in the English Language. Choose_word then appends each of the lines in to a list for random.choice to pick
    a word to be the word the user will be trying to guess. The next function I created was the check_valid function
    which would look at your input and check whether it is an actual word or not. The way the function does this is by
    adding all of the lines in five_letter_word.txt into a list and checking if the word the user inputted is in the
    list. If it is in the list than nothing happens, but if it is not in the list than the program return Not a valid
    5 letter word and prompts the user again for a word. The next function is the answer_check function which checks whether
    the word you inputted is the same as the random word that choose_word found. If it is the same the function returns
    True otherwise it returns False. The last function is called color_word which takes in two parameters, the word
    that the user is trying to guess and the users guess. The function checks whether a letter in the guess is in the
    actual word. If a letter is in the guess and it is at the same index as the letter in the actual word, the letter
    will turn green meaning that letter is correctly place. If the letter is yellow than the letter is in the word
    but it is not in the correct index. Finally if the letter is gray than the letter is not in the actual word at all.
    
    How The Game Works:
    First you type in a five letter word that might be the answer. Then you see whether there are any green or yellow
    letters. The black letters are not in the word so you should not type the letters in again. You type a five letter
    word 5 more times moving the yellow letter around and not moving the green letter until you reach the answer.