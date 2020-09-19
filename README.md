# Spammer

A simple automated message spammer that works on any messaging platform.

## Installation

- `git clone https://github.com/dmoini/spammer.git`
- `cd spammer`
- `make init`
  - It is recommended to use a [virtual environment](https://virtualenv.pypa.io/en/latest/) when installing pip packages for this.

## Usage

- `make run`
- You will be prompted to choose a way to spam.
  - For text file, you will be prompted to choose a text file from the ones in the `texts` folder.
- You will be prompted one last time to confirm that you would like to spam and instructions on how to end the program early.
  - This program mainly runs on the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) package. To end any PyAutoGUI function early, move the mouse in any of the four corners of the primary monitor.
- Once fully executed, statistics will be printed including execution time, word count, and words per minute.

## Adding Text Files

Text files can be added into the `texts` folder and will automatically be added to the command line selection. When adding a text file, name it in the following format:

`text-file-name-with-hyphens-as-spaces.txt`

## Updating Global Variables

You can update the settings via the global variables at the top of python files in the `spam` folder.
Global variables include:

- `COUNTDOWN_SECONDS`: The number of seconds for the countdown before the spamming begins.
- `MAX_REPEATED_MESSAGE_COUNT`: The max number a repeated message can be sent.
- `WORD_PROGRESS_COUNT_PROMPT_COUNT`: The count of every `n` messages sent for the user to be updated on the progress of the spammer.
- `TEXT_FILES_DIR`: Directory for text files.
