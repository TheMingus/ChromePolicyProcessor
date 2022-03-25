from os.path import isfile
from json import load, dump
from googlesearch import search

# - Introduce user to file, and get JSON data - #

print('\u001b[34mWelcome to \u001b[32;2;80;200;120mMingus\'\u001b[0m\u001b[34mChrome Policy tool!\u001b[0m')
print('To begin, please do the following:\n> Open chrome://policy\n> Select \u001b[1mExport to JSON\u001b[0m')
print('Now, paste the path to the exported file.')
userInput = input('\n\u001b[31m> ')
print('\u001b[0m')

# - Save JSON to variable `JSON` for use later in script. - #

while not isfile(userInput):
    print('Now, paste the path to the exported file.')
    userInput = input('\n\u001b[31m> ')
    print('\u001b[0m')
with open(userInput, 'r') as f: json = load(f)

# - Ask user what information they want to retrieve - #

print('Next, please select an option from the follwing list.\n')
print('\u001b[96m[0]\u001b[0m Allowed Extensions (Includes Full Names and URLs)')
print('\u001b[93mMore features to come.\u001b[m')

opt = input('\n\u001b[31m> ')
print('\u001b[0m')

if opt == '0':
    chromePolicies = json.get('chromePolicies')
    ExtensionInstallAllowlist = chromePolicies.get('ExtensionInstallAllowlist')
    value = ExtensionInstallAllowlist.get('value')
    results = []
    for extID in value:
        result = search(f'{extID} chrome web store', num_results=1)
        print(result)
        results.append(result)
        with open('results.json', 'w') as f: json.dump(results, f, indent=2)
