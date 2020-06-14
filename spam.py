import pyautogui
import time

COUNTDOWN_SECONDS = 10

# https://pypi.org/project/inquirer/


def chooseTextFile():
    pass


def main():
    file = open('./scripts/bee.txt', 'r')
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
