import os

def list_files(startpath, filename):
    file=open(filename, "w")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file.write('{}{}\n'.format(subindent, f))
    file.close()

print("start")
list_files("C:/Users/Desktop", "dd.txt")
print("done")