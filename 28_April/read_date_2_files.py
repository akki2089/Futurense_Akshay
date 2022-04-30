from tabulate import tabulate

sb1 = []
sb2 = []
with open("file1.txt","r") as file1:
    file1_content = file1.readlines()


with open("file2.txt","r") as file2:
    file2_content = file2.readlines()


print(file1_content)
print(file2_content)

for line1 in file1_content:
    if line1 not in file2_content:
        sb1.append((line1))
for line2 in file2_content:
    if line2 not in file1_content:
        sb2.append((line2))

with open("f.txt","w")as fnl:
    fnl.writelines(sb1)
    fnl.writelines(sb2)

print(tabulate(, headers=["s.no","file1",file2]))