# Date:13/08/2021
content=True
i=1
with open("log.txt","r") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Yes present in line {i}")
            
        i=+1