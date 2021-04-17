import time
import urllib.request
import pyautogui
import inquirer
import utils

IMAGE_DOWNLOAD_FOLDER = '/tmp/'


def spam_message():
    message = input('What message would you like to send?: ')
    spam_count = utils.get_spam_count()
    utils.prompt_confirmation_and_countdown()
    start_time = time.time()
    message_count = 0
    for _ in range(spam_count):
        pyautogui.write(message)
        pyautogui.press('enter')
        message_count += 1
        utils.check_and_print_progress(message_count)
    utils.print_stats(start_time, message_count)


def spam_text_file():
    file_path = utils.choose_file()
    file = open(file_path, 'r')
    utils.prompt_confirmation_and_countdown()
    word_count = 0
    start_time = time.time()
    for line in file:
        for word in line.split():
            pyautogui.write(word)
            pyautogui.press('enter')
            word_count += 1
            utils.check_and_print_progress(word_count)
    file.close()
    utils.print_stats(start_time, word_count)


def spam_image():
    spam_count = utils.get_spam_count()
    print('\n** Make sure the image is copied to your clipboard **')
    utils.prompt_confirmation_and_countdown()
    image_count = 0
    start_time = time.time()
    for _ in range(spam_count):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        image_count += 1
        utils.check_and_print_progress(image_count)
    utils.print_stats(start_time, image_count)


def spam_image_url():
    image_url = input('Image URL: ')
    image_name = image_url.split('/')[-1]
    image_path = IMAGE_DOWNLOAD_FOLDER + image_name
    urllib.request.urlretrieve(image_url, image_path)
    print(f'Downloaded image {image_name} as {image_path}')
    utils.copy_image_to_clipboard(image_path)
    spam_count = utils.get_spam_count()
    utils.prompt_confirmation_and_countdown()
    image_count = 0
    start_time = time.time()
    for _ in range(spam_count):
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        image_count += 1
        utils.check_and_print_progress(image_count)
    utils.print_stats(start_time, image_count)


def main():
    spam_functions = {
        'Image': spam_image,
        'Image URL': spam_image_url,
        'Repeated message': spam_message,
        'Text file word by word': spam_text_file
    }
    questions = [
        inquirer.List(
            'spamChoice',
            message='What would you like to spam?',
            choices=[spam_functions.keys()]
        ),
    ]
    answers = inquirer.prompt(questions)
    spam_functions[answers['spamChoice']]()


if __name__ == "__main__":
    main()
