s = [i for i in input()]
k = s.copy()
for d in range(-25,0):
    z = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(s)):
        if s[i].lower() in z:
            k[i] = z[(z.index(s[i].lower()) + d) % len(z)]
    k[0] = k[0].upper()
    print("".join(k))
