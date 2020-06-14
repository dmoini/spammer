import pyautogui
import inquirer
import time
import os

SCRIPTS_DIR = './scripts/'
COUNTDOWN_SECONDS = 10


def chooseFile():
    availableTexts = [os.path.splitext(' '.join(f.capitalize() for f in file.split('-')))[0]
                      for file in os.listdir(SCRIPTS_DIR)]
    questions = [
        inquirer.List('textFile',
                      message='What text file would you like to use?',
                      choices=availableTexts,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return SCRIPTS_DIR + answers['textFile'].replace(' ', '-').lower() + '.txt'


def main():
    filePath = chooseFile()
    file = open(filePath, 'r')
    print(f'The spamming will begin in {COUNTDOWN_SECONDS} second(s)')
    for i in range(COUNTDOWN_SECONDS, 0, -1):
        print(i)
        time.sleep(1)
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
    file.close()


if __name__ == "__main__":
    main()
