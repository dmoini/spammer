import pyautogui
import inquirer
import time
import os
import sys

COUNTDOWN_SECONDS = 10
MAX_MESSAGE_COUNT = 50
SCRIPTS_DIR = './scripts/'


def confirmationAndCountdown():
    confirmation = ''
    while True:
        confirmation = input(
            'Spamming will begin shortly. To exit script early, move your mouse to any corner of your screen. Please confirm you understand this and would like to proceed [y/n]: ').lower()
        if confirmation == 'y':
            break
        if confirmation == 'n':
            sys.exit()
    print(f'\nThe spamming will begin in {COUNTDOWN_SECONDS} second(s)')
    for i in range(COUNTDOWN_SECONDS, 0, -1):
        print(i)
        time.sleep(1)


def spamMessage():
    message = input('What message would you like to send?\n> ')
    count = 0
    while not(0 < count <= MAX_MESSAGE_COUNT):
        count = int(
            input(f'How many times would you like to send this message? (Max is {MAX_MESSAGE_COUNT})\n> '))
    print()
    confirmationAndCountdown()
    for i in range(count):
        pyautogui.write(message)
        pyautogui.press('enter')


def chooseFile():
    availableTexts = []
    for file in os.listdir(SCRIPTS_DIR):
        s = ' '.join(f.capitalize() for f in file.split('-'))
        s = os.path.splitext(s)[0]
        availableTexts.append(s)
    questions = [
        inquirer.List('textFile',
                      message='What text file would you like to use?',
                      choices=availableTexts,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return SCRIPTS_DIR + answers['textFile'].replace(' ', '-').lower() + '.txt'


def spamTextFile():
    filePath = chooseFile()
    file = open(filePath, 'r')
    confirmationAndCountdown()
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
    file.close()


def main():
    questions = [
        inquirer.List('spamChoice',
                      message='Would you like to send a repeated message or a text file word by word?',
                      choices=['Repeated message', 'Text file word by word'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers['spamChoice'] == 'Repeated message':
        spamMessage()
    else:
        spamTextFile()


if __name__ == "__main__":
    main()
