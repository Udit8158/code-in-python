# Date:13/08/2021
with open("log.txt","r") as f:
    content = f.read()
if "python" in content.lower():      #doing this to convert into lower case
    print("Yes python is present")
else:
    print("No python is not present")
