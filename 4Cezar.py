
z = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
s = [i for i in input()]
n = int(input())
for i in range(len(s)):
    if s[i].lower() in z:
        s[i] = z[(z.index(s[i].lower()) + n) % len(z)]
s[0] = s[0].upper()
print("".join(s))

