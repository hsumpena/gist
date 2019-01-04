import random
a = random.sample(range(97,123),10)
b = random.sample(range(97,123),15)
aa=[]; bb=[]
aaa=[]; bbb=[]; ccc=[]; ddd=[]
for x in a: aa.append(chr(x))
for y in b: bb.append(chr(y))
print(aa)
print(bb)
print(list(set(aa) & set(bb)))
print(list(set(aa) ^ set(bb)))
print(list(set(aa) | set(bb)))
print(list(set(aa) - set(bb)))
