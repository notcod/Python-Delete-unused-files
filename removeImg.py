import os,sys



def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


args = sys.argv

# if len(args) == 1:
#     exit('Define path!')

# root = args[1]

root = "/var/www/html"

files = []
images = []
delImgs = []

for dirpath, dirnames, filenames in os.walk(root):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        images.append((os.path.join(dirpath, filename)).replace(root, ''))


for dirpath, dirnames, filenames in os.walk(root):
    for filename in [f for f in filenames if f.endswith(".jpeg")]:
        images.append((os.path.join(dirpath, filename)).replace(root, ''))

for dirpath, dirnames, filenames in os.walk(root):
    for filename in [f for f in filenames if f.endswith(".png")]:
        images.append((os.path.join(dirpath, filename)).replace(root, ''))

for dirpath, dirnames, filenames in os.walk(root):
    for filename in [f for f in filenames if f.endswith(".svg")]:
        images.append((os.path.join(dirpath, filename)).replace(root, ''))

for dirpath, dirnames, filenames in os.walk(root):
    for filename in [f for f in filenames if f.endswith(".ico")]:
        images.append((os.path.join(dirpath, filename)).replace(root, ''))

for path, subdirs, filesX in os.walk(root):
    for name in filesX:
        file = path + "/" + name
        size = os.path.getsize(file)
        if size != 0:
            if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.svg', '.ico', '.ttf', '.eot', '.otf', '.woff', '.woff2')) and os.path.isfile(file) and os.access(file, os.R_OK):
                if ".git" not in file:
                    files.append(file)

error_files = []
len_images = len(images)
len_files = len(files)
for i in range(len_images):
    contain = False
    delImage = True
    if 'favicon' in images[i]:
        contain = True

    if '/assets/content' in images[i]:
        contain = True

    for a in range(len_files):
        try:
            if contain == False:
                contain = check_if_string_in_file(files[a], images[i])
            else:
                continue
        except:
            if files[a] not in error_files:
                error_files.append(files[a])

    if contain == True:
        delImage = False
    if delImage == True:
        delImgs.append(images[i])


print(error_files)
print(len(images))
print(len(files))
print(len(delImgs))
for i in range(len(delImgs)):
    print(delImgs[i])
    delMe = (root + "/" + delImgs[i]).replace('//', '/')
    os.remove(delMe)