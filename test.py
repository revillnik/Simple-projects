s = [i for i in input().split(" ")]
z = list("abcdefghijklmnopqrstuvwxyz")
f = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
k = []
def bykv(str):
    c = 0
    for i in str:
        if i.isalpha():
            c += 1
    return c
for d in range(len(s)):
    o = list(s[d])
    for i in range(len(o)):
        if o[i] in z:
            o[i] = z[(z.index(o[i]) + bykv(s[d])) % len(z)]
        if o[i] in f:
            o[i] = f[(f.index(o[i]) + bykv(s[d])) % len(f)]
    k.append("".join(o))
print(" ".join(k))
