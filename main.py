from os import listdir
from os.path import isfile
from json import load, dump
from tqdm import tqdm
from urllib.error import HTTPError
from urllib.request import urlretrieve, urlopen

print('Welcome to \u001b[38;2;80;200;120mMingus\'\u001b[0m Chrome Policy tool!')
print('''\n\u001b[33;1mQuick Start/First Time Instructions:\u001b[0m\n
\u001b[33m>\u001b[0;1m Open chrome://policy
\u001b[33m>\u001b[0;1m Select Export to JSON
\u001b[33m>\u001b[0;1m Place the file in the policies directory.
\u001b[33m>\u001b[0;1m If you would like to process more than one policy, place multiple files in the policies directory.''')
policy = input('\nWhen the file is in place, press enter to continue...\u001b[0m')

# using a .gitignore in the folder mucked this up, so it potentially is more complicated than it should've been

policies = listdir('policies')

if not policies:
    print('\nPolicies directory contains no files. Please add at least one policy file and try again.')
    quit()
for i in policies:
    if i[-5:] != '.json':
        print(f'\n{i} is not a JSON file, please remove it and try again.')
        quit()

print('\n\u001b[1mNext, please select an option from the follwing list.\n\u001b[0m')
print('\u001b[96;1m[0]\u001b[0;1m Gather Allowed Extension Information\n\u001b[0m    Extension IDs, Full Names, and URLs, will be saved to a file')
print('\u001b[96;1m[1]\u001b[0;1m Retrieve Login Wallpaper, and save it to a file\u001b[0m')

opt = input('\n\u001b[31m> ')
print('\u001b[0m')

if opt == '0':
    for i in policies:
        print(i)
        if i != '.gitignore':
            with open(f'policies/{i}', 'r') as f:
                policy = load(f)
            extensions = policy.get('chromePolicies').get('ExtensionInstallAllowlist').get('value')
            results = {}
            # errors = 1
            for id in tqdm(extensions):
                try:
                    url = urlopen(f'https://chrome.google.com/webstore/detail/{id}').geturl()
                    name = url.replace('https://chrome.google.com/webstore/detail/', '')
                    name.replace(f'/{id}', '')
                    name.replace('-', ' ')
                    results[id] = {'error': False, 'name': name, 'url': url}
                except urllib.error.HTTPError:
                    results[id] = {'error': True}
                    errors += 1
            with open(f'results/extensions_{i}.json', 'w') as f: dump(results, f, indent=2)
            print(f'{errors} extensions were not found. These extensions are no longer on the Chrome Web Store, for various reasons.')

elif opt == '1':
    for i in policies:
        with open(f'policies/{i}', 'r') as f:
            policy = load(f)
        wallpaper = policy.get('chromePolicies').get('DeviceWallpaperImage').get('value').get('url')
        urlretrieve(wallpaper, f'results/wallpaper_{i}.jpeg')

else:
    print('\u001b[1;31mInvalid option was selected, exiting...')