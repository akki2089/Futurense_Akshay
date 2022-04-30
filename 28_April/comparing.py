

with open("file1.txt","r") as file1:
    l1=file1.readlines()
with open("file2.txt","r") as file2:
    l2=file2.readlines()
'''print(l1)
print(len(l1))
q=l1[0]
final_list=q.split()
print(final_list)'''
f1_list=[]
f2=[]
f2_list=[]
for word in range(len(l1)):
    q=l1[word]
    print(q)
    f=q.split()
    f1_list.extend(f)
for j in range(len(l2)):
    q=l2[j]
    f2=q.split()
    f2_list.extend(f2)
print(f1_list)
print(f2_list)
for i in range(len(f1_list)):
    if f1_list[i]!=f2_list[i]:
        print("the words that mismatch are :-"+f1_list[i]+"  "+f2_list[i])

