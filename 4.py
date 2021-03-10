w=input("yek kalame ra vared konid: ")
v=["a","e","i","o","u"]
found=[]
for l in w:
    if l in v:
        if l not in found:
            found.append(l)
for vowel in found:
    print(vowel)