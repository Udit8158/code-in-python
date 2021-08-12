# Date:12/08/2021
for i in range(2,21):
    with open(f'table\multiplicationtableof{i}.txt','w') as f: #use of f string 
        for j in range(1,11):
            f.write(str(i)+" X "+str(j)+" = "+str(j*i))  #wit out use of f string.But if we use f str here it looks like   "f.write(f"{i}x{j} = {i*j}")"
            if j !=10:
                f.write('\n')    #This is for not to print 11th line in multiplication table