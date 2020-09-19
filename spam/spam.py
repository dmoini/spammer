import pyautogui
import inquirer
import time
import utils

MAX_REPEATED_MESSAGE_COUNT = 50


def spamMessage():
    message = input('What message would you like to send?: ')
    messageCount = 0
    while not(0 < messageCount <= MAX_REPEATED_MESSAGE_COUNT):
        messageCount = int(
            input(f'How many times would you like to send this message? (Max is {MAX_REPEATED_MESSAGE_COUNT}): '))

    utils.promptConfirmationAndCountdown()
    startTime = time.time()
    wordCount = 0
    for i in range(messageCount):
        pyautogui.write(message)
        pyautogui.press('enter')
        wordCount += 1
        utils.checkAndPrintProgress(wordCount)
    utils.printStats(startTime, wordCount)


def spamTextFile():
    filePath = utils.chooseFile()
    file = open(filePath, 'r')
    utils.promptConfirmationAndCountdown()
    wordCount = 0
    startTime = time.time()
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
            wordCount += 1
            utils.checkAndPrintProgress(wordCount)
    file.close()
    utils.printStats(startTime, wordCount)


def spamImage():
    messageCount = 0
    while not(0 < messageCount <= MAX_REPEATED_MESSAGE_COUNT):
        messageCount = int(
            input(f'How many times would you like to send the image? (Max is {MAX_REPEATED_MESSAGE_COUNT}): '))
    print('\n** Make sure the image you would like to spam is copied to your clipboard **')
    utils.promptConfirmationAndCountdown()
    imageCount = 0
    startTime = time.time()
    for i in range(messageCount):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        imageCount += 1
        utils.checkAndPrintProgress(imageCount)
    utils.printStats(startTime, imageCount)


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
