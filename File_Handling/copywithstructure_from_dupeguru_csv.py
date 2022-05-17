# I need this because Skyrim has some necessary duplicates in the terrain folder. (2+ GB for HD textures!)
# So I removed the dupes but kept a record of them so I can repopulate the folder with them once they've been processed.
# All this does is make copies of the 'first' instance of an image, as such 'duplicate' instances. Therefore
# Repopulating the folder as the game needs to function.

import pandas as pd
from shutil import copyfile


# Read csv of duplicate information.
csv_file = 'dupes.csv'
df = pd.read_csv(csv_file, usecols=['Group ID', 'Filename', 'Folder'])

# Create the Name (Folder path + file name)
df['Name'] = df['Folder'] + '\\' + df['Filename']

# Add entries to the dictionary under key as 'ID', and value as a list of 'Name's.
counter = -1
dupe_dict = {}
for index, row in df.iterrows():
    if counter != row['Group ID']:
        counter = row['Group ID']
        dupe_dict[row['Group ID']] = [row['Name']]
    else:
        dupe_dict[row['Group ID']].append(row['Name'])

# For each key [ID] copy the first (original) to value all other values. This repopulates
# the dupes so the game is happy :-). Ignores when the original tries to overwrite itself.
for key, value in dupe_dict.items():
    for index in range(len(value)):
        try:
            copyfile(value[0], value[index])
            print('cp ' + value[0], value[index])
        except IOError:
            print('cp fail' + value[0], value[index])
            pass
        
