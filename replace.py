a=str(input())
t=str(input())
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
c=max(dict,key=dict.get)
print(a.replace(c,t))
        


