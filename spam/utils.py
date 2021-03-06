import inquirer
import os
import sys
import time

COUNTDOWN_SECONDS = 10
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
