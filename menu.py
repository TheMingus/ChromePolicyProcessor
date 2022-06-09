from os import get_terminal_size

# -- # Set menu items here! #--#
# -- # Index: Option number #--#
# -- # Key: Name of option #--#
# -- # Value: Description of option #--#

menu = {
    'Extension Info': 'Gather Whitelisted Extension Information|Extension IDs, Full Names, and URLs, will be saved to a file'
}

lines = get_terminal_size().lines
columns = get_terminal_size().columns

extraTop = (lines-len(menu))/2
extraSides = (columns-len(menu))/2


# -- # Final Printing # -- #

print('\n'*extraTop)
