import pyautogui
import inquirer
import time

COUNTDOWN_SECONDS = 10


def chooseTextFile():
    questions = [
        inquirer.List('textFile',
                      message='What text file would you like to spam?',
                      choices=['Bee Movie'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['textFile'].replace(' ', '-').lower()


def main():
    filePath = './scripts/' + chooseTextFile() + '.txt'
    file = open(filePath, 'r')
    print(f'The spamming will begin in {COUNTDOWN_SECONDS} second(s)')
    for i in range(COUNTDOWN_SECONDS, 0, -1):
        print(f'{i}')
        time.sleep(1)
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
    file.close()


if __name__ == "__main__":
    main()
