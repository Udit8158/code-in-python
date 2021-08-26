# Date:13/08/2021
with open("this.txt") as f:
    content_1=f.read()
with open("copied.txt") as f:
    content_2=f.read()
if content_1==content_2:
    print("Yes content of these two files are identical")
else:
    print("No content of these two files are not identical")
