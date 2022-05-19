from os import listdir
from os.path import isfile
from json import load, dump
import urllib.request
from tqdm import tqdm

print('Welcome to \u001b[38;2;80;200;120mMingus\'\u001b[0m Chrome Policy tool!')
print('''Quick Start/First Time Instructions:
> Open chrome://policy
> Select \u001b[1mExport to JSON\u001b[0m
> Place the file in the policies directory.

> If you would like to process more than one policy, place multiple files in the policies directory.''')
policy = input('\nWhen the file is in place, press enter to continue...')

# if isfile('policies.json'):
#     policy = 'policies.json'
# elif not isfile('policies.json'):
#     while not isfile(policy):
#         print('File was not found in the script directory. Please input the policy file\'s path')
#         policy = input('\n> ')
for i in listdir('policies'):
    if '.json' != i[-5:]:
        print(f'{i} is not a JSON file, please remove it.')
        quit()

print('Next, please select an option from the follwing list.\n')
print('\u001b[96m[0]\u001b[0m Gather Allowed Extension Information\n    Extension IDs, Full Names, and URLs, will be saved to a file')
print('\n\u001b[93mMore features to come.\u001b[m')

opt = input('\n\u001b[31m> ')
print('\u001b[0m')

if opt == '0':
    extensions = policy.get('chromePolicies').get('ExtensionInstallAllowlist').get('value')
    results = {}
    errors = []
    for id in tqdm(extensions):
        try:
            url = urllib.request.urlopen(f'https://chrome.google.com/webstore/detail/{id}').geturl()
            name = url.replace('https://chrome.google.com/webstore/detail/', '')
            name = name.replace(f'/{id}', '')
            name.replace('-', ' ')
            results[id] = {'error': False, 'name': name, 'url': url}
        except urllib.error.HTTPError:
            results[id] = {'error': True}
            errors.append(id)
    # if isfile(f'results/{}'):
    with open('results/extensions.json', 'w') as f: dump(results, f, indent=2)
    print(f'{len(errors)} extensions were not found. These extensions are no longer on the Chrome Web Store, for various reasons.')
