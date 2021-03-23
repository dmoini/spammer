import pyautogui
import inquirer
import time
import urllib.request
import utils

IMAGE_DOWNLOAD_FOLDER = '/tmp/'


def spamMessage():
    message = input('What message would you like to send?: ')
    spamCount = utils.getSpamCount()
    utils.promptConfirmationAndCountdown()
    startTime = time.time()
    messageCount = 0
    for i in range(spamCount):
        pyautogui.write(message)
        pyautogui.press('enter')
        messageCount += 1
        utils.checkAndPrintProgress(messageCount)
    utils.printStats(startTime, messageCount)


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
    spamCount = utils.getSpamCount()
    print('\n** Make sure the image is copied to your clipboard **')
    utils.promptConfirmationAndCountdown()
    imageCount = 0
    startTime = time.time()
    for i in range(spamCount):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        imageCount += 1
        utils.checkAndPrintProgress(imageCount)
    utils.printStats(startTime, imageCount)


def spamImageUrl():
    imageUrl = input('Image URL: ')
    imageName = imageUrl.split('/')[-1]
    imagePath = IMAGE_DOWNLOAD_FOLDER + imageName
    urllib.request.urlretrieve(imageUrl, imagePath)
    print(f'Downloaded image {imageName} as {imagePath}')
    utils.copyImageToClipboard(imagePath)
    spamCount = utils.getSpamCount()
    utils.promptConfirmationAndCountdown()
    imageCount = 0
    startTime = time.time()
    for i in range(spamCount):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        imageCount += 1
        utils.checkAndPrintProgress(imageCount)
    utils.printStats(startTime, imageCount)


def main():
    spamFunctions = {
        'Image': spamImage,
        'Image URL': spamImageUrl,
        'Repeated message': spamMessage,
        'Text file word by word': spamTextFile
    }
    questions = [
        inquirer.List(
            'spamChoice',
            message='What would you like to spam?',
            choices=[key for key in spamFunctions.keys()]
        ),
    ]
    answers = inquirer.prompt(questions)
    spamFunctions[answers['spamChoice']]()


if __name__ == "__main__":
    main()
