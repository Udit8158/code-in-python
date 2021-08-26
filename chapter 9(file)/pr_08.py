# Date:13/08/2021
# Copied a file content to another
with open("this.txt")as f:
    content=f.read()
with open("copied.txt","w") as f:
    f.write(content)