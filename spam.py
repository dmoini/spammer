import pyautogui
import inquirer
import time
import os
import sys

COUNTDOWN_SECONDS = 10
MAX_REPEATED_MESSAGE_COUNT = 50
PROGRESS_CHECK_COUNT = 100
TEXT_FILES_DIR = './texts/'


def promptConfirmationAndCountdown():
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
        print(f'{i}', end=' ', flush=True)
        time.sleep(1)
    print()


def checkAndPrintProgress(count):
    if count % PROGRESS_CHECK_COUNT == 0:
        print(f'{count} words/images sent')


def printStats(startTime, count):
    totalSeconds = time.time() - startTime
    spamPerMinute = count / (totalSeconds / 60)
    print(f'\nExecution time: {totalSeconds:.2f} second(s)')
    print(f'Word/image count: {count}')
    print(f'Words/Images per minute: {spamPerMinute:.2f}')


def spamMessage():
    message = input('What message would you like to send?: ')
    messageCount = 0
    while not(0 < messageCount <= MAX_REPEATED_MESSAGE_COUNT):
        messageCount = int(
            input(f'How many times would you like to send this message? (Max is {MAX_REPEATED_MESSAGE_COUNT}): '))
    promptConfirmationAndCountdown()
    startTime = time.time()
    wordCount = 0
    for i in range(messageCount):
        pyautogui.write(message)
        pyautogui.press('enter')
        wordCount += 1
        checkAndPrintProgress(wordCount)
    printStats(startTime, wordCount)


def chooseFile():
    availableTexts = []
    for file in os.listdir(TEXT_FILES_DIR):
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
    return TEXT_FILES_DIR + answers['textFile'].replace(' ', '-').lower() + '.txt'


def spamTextFile():
    filePath = chooseFile()
    file = open(filePath, 'r')
    promptConfirmationAndCountdown()
    wordCount = 0
    startTime = time.time()
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
            wordCount += 1
            checkAndPrintProgress(wordCount)
    file.close()
    printStats(startTime, wordCount)


def spamImage():
    messageCount = 0
    while not(0 < messageCount <= MAX_REPEATED_MESSAGE_COUNT):
        messageCount = int(
            input(f'How many times would you like to send the image? (Max is {MAX_REPEATED_MESSAGE_COUNT}): '))
    print('\n** Make sure the image you would like to spam is copied to your clipboard **')
    promptConfirmationAndCountdown()
    imageCount = 0
    startTime = time.time()
    for i in range(messageCount):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        imageCount += 1
        checkAndPrintProgress(imageCount)
    printStats(startTime, imageCount)


def main():
    questions = [
        inquirer.List('spamChoice',
                      message='What would you like to spam?',
                      choices=['Image', 'Repeated message',
                               'Text file word by word'],
                      ),
    ]
    spamFunctions = {'Image': spamImage,
                     'Repeated message': spamMessage,
                     'Text file word by word': spamTextFile}
    answers = inquirer.prompt(questions)
    spamFunctions[answers['spamChoice']]()


if __name__ == "__main__":
    main()
