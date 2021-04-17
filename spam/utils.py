import os
import subprocess
import sys
import time
import inquirer

COUNTDOWN_SECONDS = 10
MAX_SPAM_COUNT = 50
PROGRESS_CHECK_COUNT = 100
SPAM_COUNT_PROMPT = f'How many times? (Max is {MAX_SPAM_COUNT}): '
SPAM_CONFIRMATION = '\nSpamming will begin shortly. To exit the script early, move your' + \
    ' mouse to any corner of the screen.\n\nWould you like to proceed [y/n]: '
TEXT_FILES_DIR = './texts/'


def get_spam_count():
    spam_count = 0
    while not 0 < spam_count <= MAX_SPAM_COUNT:
        spam_count = int(input(SPAM_COUNT_PROMPT))
    return spam_count


def prompt_confirmation_and_countdown():
    confirmation = ''
    while True:
        confirmation = input(SPAM_CONFIRMATION).lower()
        if confirmation == 'y':
            break
        if confirmation == 'n':
            sys.exit()
    print(f'\nThe spamming will begin in {COUNTDOWN_SECONDS} second(s)')
    for i in range(COUNTDOWN_SECONDS, 0, -1):
        print(f'{i}', end=' ', flush=True)
        time.sleep(1)
    print()


def check_and_print_progress(count):
    if count % PROGRESS_CHECK_COUNT == 0:
        print(f'{count} words/images sent')


def print_stats(start_time, count):
    total_seconds = time.time() - start_time
    spam_per_minute = count / (total_seconds / 60)
    print(f'\nExecution time: {total_seconds:.2f} second(s)')
    print(f'Word/image count: {count}')
    print(f'Words/Images per minute: {spam_per_minute:.2f}')


def choose_file():
    available_texts = []
    for file in os.listdir(TEXT_FILES_DIR):
        text_file_name = ' '.join(f.capitalize() for f in file.split('-'))
        text_name = os.path.splitext(text_file_name)[0]
        available_texts.append(text_name)
    questions = [
        inquirer.List(
            'textFile',
            message='What text file would you like to use?',
            choices=available_texts,
        ),
    ]
    answers = inquirer.prompt(questions)
    return TEXT_FILES_DIR + answers['textFile'].replace(' ', '-').lower() + '.txt'


def copy_image_to_clipboard(image_path):
    args = [
        'osascript',
        '-e',
        f'set the clipboard to (read (POSIX file \"{image_path}\") as JPEG picture)'
    ]
    subprocess.run(args, check=True)
