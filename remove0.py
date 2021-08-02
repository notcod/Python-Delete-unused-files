import sys
import os
import inquirer

delFolders = True
delFiles = True

folderD = '_delete'
files = []
folders = []
args = sys.argv

if len(args) == 1:
    exit('Define path and what to delete! ' +
         args[0] + " /path/to/where -fd (files and directories)/ -f (files)/ -d(directories)")

if len(args) == 3:
    if args[2].lower() == "-f":
        delFolders = False

    if args[2].lower() == "-d":
        delFolders = False

root = args[1]
isFolder = os.path.isdir(root)
if isFolder == False:
    exit("Folder doesn't exist!")

for path, subdirs, filesX in os.walk(root):
    if delFolders == True:
        if len(os.listdir(path)) == 0:
            folder_path = path.replace(root, '')
            if folderD not in folder_path:
                folders.append(folder_path)

    if delFiles == True:
        for name in filesX:
            file = path + "/" + name
            size = os.path.getsize(file)
            if size == 0:
                file_path = file.replace(root, '')
                if folderD not in file_path:
                    files.append(file_path)

if len(files) > 0 or len(folders) > 0:
    if delFolders == True:
        print()
        print("Folders:")
        print(folders)
    if delFiles == True:
        print()
        print("Files:")
        print(files)
    print()
    questions = [inquirer.List('action', message="Choose action on files: ", choices=[
                               'Move all to ' + folderD + '/*', 'Delete all', 'Nothing'])]
    answers = inquirer.prompt(questions)
    inputer = answers["action"]
    if inputer == "Move all to " + folderD + "/*":
        for i in range(len(files)):
            old_path = (root + "/" + files[i]).replace('//', '/')
            print(old_path)
            new_path = (root + "/" + folderD + "/" +
                        files[i]).replace('//', '/')
            new_path_root = new_path.split("/")
            new_path_root.pop()
            new_path_root = '/'.join(new_path_root)
            if os.path.isdir(new_path_root) == False:
                os.makedirs(new_path_root)
            os.rename(old_path, new_path)

        for i in range(len(folders)):
            old_path = (root + "/" + folders[i]).replace('//', '/')
            new_path = (root + "/" + folderD + "/" + folders[i]).replace('//', '/')
            print(new_path)
            if os.path.isdir(new_path) == False:
                os.makedirs(new_path)
            os.rmdir(old_path)

        print("Moving is done!")
    elif inputer == "Delete all":
        for i in range(len(files)):
            old_path = (root + "/" + files[i]).replace('//', '/')
            os.remove(old_path)

        for i in range(len(folders)):
            Folder = (root + "/" + folders[i]).replace('//', '/')
            os.rmdir(Folder)

        print("Deleting is done!")
else:
    print("Nothing to move!")
