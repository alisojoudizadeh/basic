w=input("yek kalame ra vared konid: ")
v=["a","e","i","o","u"]
found={}
found["a"]=0
found["e"]=0
found["i"]=0
found["o"]=0
found["u"]=0
for l in w:
    if l in v:
        found[l] += 1
for k,v in found.items():
    print(k," was found ",v,"time(s)")