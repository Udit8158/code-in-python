# Date:13/08/2021
import os
with open("fileforpr_11.txt")as f:
    content_1=f.read()
with open("renamed_by_python.txt","w")as f:
    f.write(content_1)
os.remove("fileforpr_11.txt") #This for deleting a existing file
# To cheeck the whole programme again make a file name "fileforpr_11.txt" because this file was deleted now.
