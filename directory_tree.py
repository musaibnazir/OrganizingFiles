import os

for folderName, subfolders, filename in os.walk(''):
    print('The current folder is ', folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF' + foldername + ':' + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + folderName + ':' + filename)

    print('')        
