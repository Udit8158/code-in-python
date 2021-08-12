# Date:12/08/2021
with open("poem.txt",'r') as f:
    a=f.read()
print(a)
if "Twinkle" in a:
    print("Yes Twinkle is present in the text")
else:
    print("No Twinkle is not present in the text")

    