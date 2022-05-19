from os import listdir
from os.path import isfile
from json import load, dump
import urllib.request
from tqdm import tqdm
from urllib.request import urlretrieve

print('Welcome to \u001b[38;2;80;200;120mMingus\'\u001b[0m Chrome Policy tool!')
print('''Quick Start/First Time Instructions:
> Open chrome://policy
> Select \u001b[1mExport to JSON\u001b[0m
> Place the file in the policies directory.

> If you would like to process more than one policy, place multiple files in the policies directory.''')
policy = input('\nWhen the file is in place, press enter to continue... ')

if not listdir('policies'):
    print('\nPolicies directory contains no files. Please add a policy file.')
    quit()
policies = listdir('policies')
del policies[-1:]
for i in policies:
    if '.json' != i[-5:] and i != '.gitignore':
        print(f'\n{i} is not a JSON file, please remove it.')
        quit()

print('Next, please select an option from the follwing list.\n')
print('\u001b[96m[0]\u001b[0m Gather Allowed Extension Information\n    Extension IDs, Full Names, and URLs, will be saved to a file')
print('\u001b[96m[1]\u001b[0m Retrieve Login Wallpaper, and save it to a file')
print('\n\u001b[93mMore features to come.\u001b[m')

opt = input('\n\u001b[31m> ')
print('\u001b[0m')

if opt == '0':
    for i in policies:
        with open(f'policies/{i}', 'r') as f:
            policy = load(f)
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
        with open(f'results/extensions_{i}.json', 'w') as f: dump(results, f, indent=2)
        print(f'{len(errors)} extensions were not found. These extensions are no longer on the Chrome Web Store, for various reasons.')

if opt == '1':
    for i in policies:
        with open(f'policies/{i}', 'r') as f:
            policy = load(f)
        wallpaper = policy.get('chromePolicies').get('DeviceWallpaperImage').get('value').get('url')
        urlretrieve(wallpaper, f'results/wallpaper_{i}.jpeg')
