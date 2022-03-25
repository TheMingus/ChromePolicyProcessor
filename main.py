from os.path import isfile
from json import load

# - Introduce user to file, and get JSON data - #

print('\u001b[34mWelcome to \u001b[32;2;80;200;120mMingus\'\u001b[0m\u001b[34mChrome Policy tool!\u001b[0m')
print('To begin, please do the following:\n> Open chrome://policy\n> Select either \u001b[1mCopy as JSON\u001b[0m or \u001b[1mExport to JSON\u001b[0m')
print('> If you selected \u001b[1mCopy as JSON\u001b[0m, paste your clipboard contents here. If you selected \u001b[1mExport to JSON\u001b[0m, paste the path to the exported file.')
userInput = input('\n\u001b[31m> ')
print('\u001b[0m')

# - Save JSON to variable `JSON` for use later in script. - #

if isfile(userInput):
    with open(userInput, 'r') as f: json = load(f)
else:
    json = userInput

# - Ask user what information they want to retrieve - #

print('Next, please select an option from the follwing list.\n')
print('\u001b[96m[0]\u001b[0m Allowed Extensions (Includes Full Names and URLs)')
print('\u001b[93mMore features to come.\u001b[m')