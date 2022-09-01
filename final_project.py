import random
from colorama import Fore
import re

'''
This is a wordle remake. You have six tries to guess a random five letter word.
'''


def main():
    actual_word = choose_word().upper()
    ans = ''
    previous_ans = []
    i = 6
    while i > 0:
        while True:
            try:
                ans = input(Fore.WHITE + f'You have {i} guesses left. Type your guess: ').upper()
                if check_valid(ans) == "Not a valid 5 letter word":
                    raise ValueError
            except ValueError:
                print('Not a valid 5 letter word')
                pass
            else:
                break
        i -= 1
        if answer_check(actual_word, ans):
            print(color_word(actual_word, ans))
            break
        else:
            if len(previous_ans) != 0:
                for j in range(len(previous_ans)):
                    print(previous_ans[j])
                print(color_word(actual_word, ans))
                previous_ans.append(color_word(actual_word, ans))
            else:
                print(color_word(actual_word, ans))
                previous_ans.append(color_word(actual_word, ans))
    if ans == actual_word:
        print(Fore.BLUE + 'Congratulations you got the answer')
    else:
        print(Fore.RED + f'The word was {actual_word}')


def choose_word():
    with open('five_letter_word') as file:
        lines = file.readlines()

    all_words = []
    for line in lines:
        all_words.append(line.rstrip())

    return random.choice(all_words)


def check_valid(answer):
    with open('five_letter_word') as file:
        lines = file.readlines()

    all_words = []
    for line in lines:
        all_words.append(line.rstrip().upper())

    if answer in all_words:
        pass
    else:
        return "Not a valid 5 letter word"


def answer_check(the_word, answer):
    if the_word == answer:
        return True
    else:
        return False


def color_word(the_word, answer):
    pretty = ''
    amount_correct = 0
    for c in range(len(the_word)):
        if answer[c] in the_word and the_word[c] == answer[c]:
            pretty = pretty + f"{Fore.GREEN + answer[c]} "
            amount_correct += 1
        elif answer[c] in the_word:
            if len(re.findall(rf'{answer[c]}', answer)) == len(re.findall(rf'{answer[c]}', the_word)):
                pretty = pretty + f'{Fore.YELLOW + answer[c]} '

            elif len(re.findall(rf'{answer[c]}', answer)) > len(re.findall(rf'{answer[c]}', the_word)):
                amount_extra = len(re.findall(rf'{answer[c]}', answer)) - len(re.findall(rf'{answer[c]}', the_word))
                # check before code
                if answer.find(answer[c]) == c and amount_extra <= 1:
                    pretty = pretty + f"{Fore.WHITE + answer[c]} "
                    amount_extra -= 1
                elif answer.find(answer[c]) != c:
                    if answer.find(answer[c]) > c:
                        pretty = pretty + f'{Fore.YELLOW + answer[c]} '
                    else:
                        if answer.find(answer[c]) < c and amount_correct > 1:
                            pretty = pretty + f'{Fore.YELLOW + answer[c]} '
                        else:
                            pretty = pretty + f'{Fore.WHITE + answer[c]} '
                else:
                    # check after code
                    if answer.find(answer[c]) == c:
                        pretty = pretty + f'{Fore.YELLOW + answer[c]} '
                    else:
                        pretty = pretty + f"{Fore.WHITE + answer[c]} "

            elif len(re.findall(rf'{answer[c]}', answer)) < len(re.findall(rf'{answer[c]}', the_word)):
                pretty = pretty + f'{Fore.YELLOW + answer[c]} '
            else:
                pretty = pretty + f"{Fore.WHITE + answer[c]} "

        else:
            pretty = pretty + f"{Fore.WHITE + answer[c]} "

    return pretty


if __name__ == "__main__":
    main()
